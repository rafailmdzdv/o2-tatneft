import enum

from django.forms.models import model_to_dict

from backend import models


class FuelTypes(enum.StrEnum):
    AI92_TANEKO = 'АИ-92 Танеко'
    AI92 = 'АИ-92'
    AI95_TANEKO = 'АИ-95 Танеко'
    AI95 = 'АИ-95'
    DT = 'ДТ'
    DT_TANEKO = 'ДТ Танеко'
    AI98_TANEKO = 'АИ-98 Танеко'
    SUG = 'СУГ'
    AI98 = 'АИ-98'
    ELECTRO = 'Электрозарядка'
    AI100 = 'АИ-100'
    AD_BLUE = 'AdBlue'
    AI80 = 'АИ-80'
    DT_WINTER = 'ДТ (зимнее)'
    KPG = 'КПГ'
    DT_ARCTICA = 'ДТ Арктика'


def to_float(price_str: str | None) -> float | None:
    """
    Переводит цену из таблицы в число с плавающей точкой.
    В случаеесли цена не указана, возвращает None
    """
    if not price_str:
        return
    processed_price_str = ''
    for char in price_str:
        if char in ' ' or char.isalpha():
            break
        processed_price_str += char
    return float(processed_price_str)


def prices_to_str(gas_station: models.GasStation) -> str:
    """Возвращает список цен в приемлемом виде"""
    parsed_answer = ''
    prices_model = models.FuelPrices.objects.get(gas_station=gas_station.id)
    prices_dict = _convert_prices_model_to_dict(prices_model)
    fuel_types_dict = {i.name.lower(): i.value for i in FuelTypes}
    for name, price in prices_dict.items():
        if price is None:
            parsed_answer += f'{fuel_types_dict[name]}: -<br>'
        else:
            parsed_answer += f'{fuel_types_dict[name]}: {price}р.<br>'
    return parsed_answer


def _convert_prices_model_to_dict(prices_model: models.FuelPrices) -> dict:
    """Конвертирует модель в словарь для более удобного пользования"""
    prices_dict = model_to_dict(prices_model)
    exclude_fields = ['gas_station', 'id']
    for field in list(prices_dict):
        if field in exclude_fields:
            prices_dict.pop(field)
    return prices_dict
