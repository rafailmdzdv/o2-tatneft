from django.forms.models import model_to_dict
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
import pandas as pd

from backend import models
from o2_site import settings


FIELDS = ['Регион', 'Широта', 'Долгота', 'Номер эмитента', 'Номер АЗС',
          'Объекты', 'Услуги', 'АИ-92 Танеко', 'АИ-92', 'АИ-95 Танеко',
          'АИ-95', 'ДТ', 'ДТ Танеко', 'АИ-98 Танеко', 'СУГ', 'АИ-98',
          'Электрозарядка', 'АИ-100', 'Ad Blue', 'АИ-80', 'ДТ (зимнее)',
          'КПГ', 'ДТ Арктика']


def get_azs_xls() -> str:
    rows = _get_gas_stations_data()
    df = pd.DataFrame(rows, columns=FIELDS)

    excel_path = f'{settings.EXCELS_DIR}/azsList.xlsx'
    df.to_excel(excel_path, index=False)
    _adjust_rows_columns(excel_path)
    return excel_path


def _get_gas_stations_data() -> list:
    gas_stations = models.GasStation.objects.all()
    raw_rows = []
    for gas_station in gas_stations:
        gas_station_data = _get_raw_gs_list(gas_station)
        raw_rows.append(gas_station_data)
    return raw_rows


def _get_raw_gs_list(gas_station: models.GasStation) -> list:
    gas_station_data = _get_gs_values(gas_station)
    region = _get_region_name(gas_station)
    fuel_prices = _get_fuel_prices(gas_station)
    gas_station_data.insert(0, region)
    gas_station_data.extend(fuel_prices)
    return gas_station_data


def _get_gs_values(gas_station: models.GasStation) -> list:
    exclude_fields = ['id', 'region']
    formatted_values_dict = model_to_dict(
        gas_station,
        fields=[field.name for field in gas_station._meta.fields
                if field.name not in exclude_fields]
    )
    return list(formatted_values_dict.values())


def _get_region_name(gas_station: models.GasStation) -> str:
    region = models.Region.objects.get(pk=gas_station.region.id)
    return region.name


def _get_fuel_prices(gas_station: models.GasStation) -> list:
    exclude_fields = ['id', 'gas_station']
    fuel_prices = models.FuelPrices.objects.get(gas_station=gas_station)
    formatted_values_dict = model_to_dict(
        fuel_prices,
        fields=[field.name for field in fuel_prices._meta.fields
                if field.name not in exclude_fields]
    )
    return list(formatted_values_dict.values())


def _adjust_rows_columns(excel_path: str) -> None:
    workbook = openpyxl.load_workbook(excel_path)
    sheet = workbook.active

    _adjust_rows_height(sheet)
    _adjust_columns_width(sheet)

    workbook.save(excel_path)


def _adjust_rows_height(sheet: Worksheet) -> None:
    for index, _ in enumerate(sheet.rows, start=1):
        sheet.row_dimensions[index].auto_size = True


def _adjust_columns_width(sheet: Worksheet) -> None:
    for column in sheet.columns:
        max_length = 0
        column_letter = column[0].column_letter

        for cell in column:
            max_cell_phraze = max(str(cell.value).split('\n'))
            max_cell_phraze_len = len(max_cell_phraze)
            if max_cell_phraze_len > max_length:
                max_length = max_cell_phraze_len

        adjusted_length = max_length + 2
        sheet.column_dimensions[column_letter].width = adjusted_length
