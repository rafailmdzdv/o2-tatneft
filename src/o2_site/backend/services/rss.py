import re
import time
from urllib import request

import numpy as np
import pandas as pd
import progressbar
import schedule
import xlrd

from backend import models
from backend.utils import price
from o2_site import settings
from project_config.log import logger as log


FUEL_TYPE_LIST = [
    'АИ-92 Танеко', 'АИ-92', 'АИ-95 Танеко', 'АИ-95',
    'АИ-98 Танеко', 'АИ-98', 'ДТ', 'ДТ ТАНЕКО', 'СУГ',
    'Электрозарядка', 'АИ-100', 'AdBlue', 'АИ-80',
    'КПГ', 'ДТ (зимнее)', 'ДТ Арктика'
]


def start_monthly_parsing():
    schedule.every(30).days.do(_get_gs_data)
    log.debug('Monthly work started!')
    while True:
        schedule.run_pending()
        time.sleep(1)


def _get_gs_data():
    downloaded_file = _download_gs_xls()
    _parse_downloaded_file(downloaded_file)


def _download_gs_xls() -> str:
    return request.urlretrieve(settings.XLS_LINK, settings.XLS_FILEPATH)[0]


def _parse_downloaded_file(file_path: str):
    workbook = _get_workbook(file_path)
    log.debug('Starting interact with workbook')
    for _, row in progressbar.progressbar(workbook.iterrows()):
        region = _add_or_get_region(row)
        gas_station = _add_or_get_gas_station(region, row)
        _add_or_update_fuel_prices(gas_station, row)


def _get_workbook(file_path: str) -> pd.DataFrame:
    excel_file = xlrd.open_workbook(file_path, ignore_workbook_corruption=True)
    pd_excel = pd.read_excel(excel_file).replace(np.nan, None)
    return pd_excel


def _add_or_get_region(row: pd.Series) -> models.Region:
    region, _ = models.Region.objects.get_or_create(
        name=row['Регион']
    )
    return region


def _add_or_get_gas_station(region: models.Region,
                            row: pd.Series) -> models.GasStation:
    gas_station, _ = models.GasStation.objects.get_or_create(
        latitude=row['Координаты GPS (широта)'],
        longitude=row['Координаты GPS (долгота)'],
        issuer_number=row['Номер эмитента'],
        gs_number=int(re.search(r'\d+', row['Номер АЗС']).group(0)),
        companion_service_objects=row['Объекты сопутствующего сервиса'],
        additional_services=row['Дополнительные услуги'],
        region=region
    )
    return gas_station


def _add_or_update_fuel_prices(gas_station: models.GasStation,
                               row: pd.Series) -> None:
    fuels = {name: price.to_float(fuel_price)
             for name, fuel_price in row.items()
             if name in FUEL_TYPE_LIST}
    fuel, created = models.FuelPrices.objects.get_or_create(
        gas_station=gas_station,
        defaults={
            'ai92_taneko': fuels['АИ-92 Танеко'],
            'ai92': fuels['АИ-92'],
            'ai95_taneko': fuels['АИ-95 Танеко'],
            'ai95': fuels['АИ-95'],
            'dt': fuels['ДТ'],
            'dt_taneko': fuels['ДТ ТАНЕКО'],
            'ai98_taneko': fuels['АИ-98 Танеко'],
            'sug': fuels['СУГ'],
            'ai98': fuels['АИ-98'],
            'electro': fuels['Электрозарядка'],
            'ai100': fuels['АИ-100'],
            'ad_blue': fuels['AdBlue'],
            'ai80': fuels['АИ-80'],
            'dt_winter': fuels['ДТ (зимнее)'],
            'kpg': fuels['КПГ'],
            'dt_arctica': fuels['ДТ Арктика']
        }
    )
    if not created:
        fuel.ai92_taneko = fuels['АИ-92 Танеко']
        fuel.ai92 = fuels['АИ-92']
        fuel.ai95_taneko = fuels['АИ-95 Танеко']
        fuel.ai95 = fuels['АИ-95']
        fuel.dt = fuels['ДТ']
        fuel.dt_taneko = fuels['ДТ ТАНЕКО']
        fuel.ai98_taneko = fuels['АИ-98 Танеко']
        fuel.sug = fuels['СУГ']
        fuel.ai98 = fuels['АИ-98']
        fuel.electro = fuels['Электрозарядка']
        fuel.ai100 = fuels['АИ-100']
        fuel.ad_blue = fuels['AdBlue']
        fuel.ai80 = fuels['АИ-80']
        fuel.dt_winter = fuels['ДТ (зимнее)']
        fuel.kpg = fuels['КПГ']
        fuel.dt_arctica = fuels['ДТ Арктика']
        fuel.save()
