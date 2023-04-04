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
             if name in list(price.FuelTypes)}
    fuel, created = models.FuelPrices.objects.get_or_create(
        gas_station=gas_station,
        defaults={
            'ai92_taneko': fuels[price.FuelTypes.AI92_TANEKO],
            'ai92': fuels[price.FuelTypes.AI92],
            'ai95_taneko': fuels[price.FuelTypes.AI95_TANEKO],
            'ai95': fuels[price.FuelTypes.AI95],
            'dt': fuels[price.FuelTypes.DT],
            'dt_taneko': fuels[price.FuelTypes.DT_TANEKO],
            'ai98_taneko': fuels[price.FuelTypes.AI98_TANEKO],
            'sug': fuels[price.FuelTypes.SUG],
            'ai98': fuels[price.FuelTypes.AI98],
            'electro': fuels[price.FuelTypes.ELECTRO],
            'ai100': fuels[price.FuelTypes.AI100],
            'ad_blue': fuels[price.FuelTypes.AD_BLUE],
            'ai80': fuels[price.FuelTypes.AI80],
            'dt_winter': fuels[price.FuelTypes.DT_WINTER],
            'kpg': fuels[price.FuelTypes.KPG],
            'dt_arctica': fuels[price.FuelTypes.DT_ARCTICA]
        }
    )
    if not created:
        fuel.ai92_taneko = fuels[price.FuelTypes.AI92_TANEKO]
        fuel.ai92 = fuels[price.FuelTypes.AI92]
        fuel.ai95_taneko = fuels[price.FuelTypes.AI95_TANEKO]
        fuel.ai95 = fuels[price.FuelTypes.AI95]
        fuel.dt = fuels[price.FuelTypes.DT]
        fuel.dt_taneko = fuels[price.FuelTypes.DT_TANEKO]
        fuel.ai98_taneko = fuels[price.FuelTypes.AI98_TANEKO]
        fuel.sug = fuels[price.FuelTypes.SUG]
        fuel.ai98 = fuels[price.FuelTypes.AI98]
        fuel.electro = fuels[price.FuelTypes.ELECTRO]
        fuel.ai100 = fuels[price.FuelTypes.AI100]
        fuel.ad_blue = fuels[price.FuelTypes.AD_BLUE]
        fuel.ai80 = fuels[price.FuelTypes.AI80]
        fuel.dt_winter = fuels[price.FuelTypes.DT_WINTER]
        fuel.kpg = fuels[price.FuelTypes.KPG]
        fuel.dt_arctica = fuels[price.FuelTypes.DT_ARCTICA]
        fuel.save()
