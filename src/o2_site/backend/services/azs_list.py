import pathlib

from django.forms.models import model_to_dict

from backend import models
from backend.utils import excel


FIELDS = ['Регион', 'Широта', 'Долгота', 'Номер эмитента', 'Номер АЗС',
          'Объекты', 'Услуги', 'АИ-92 Танеко', 'АИ-92', 'АИ-95 Танеко',
          'АИ-95', 'ДТ', 'ДТ Танеко', 'АИ-98 Танеко', 'СУГ', 'АИ-98',
          'Электрозарядка', 'АИ-100', 'Ad Blue', 'АИ-80', 'ДТ (зимнее)',
          'КПГ', 'ДТ Арктика']


def get_azs_xls() -> pathlib.Path:
    rows = _get_gas_stations_data()
    excel_path = excel.save_data_to_excel(rows, 'azsList', FIELDS)
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
