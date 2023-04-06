from typing import Literal

import httpx

from backend.utils import dt
from o2_site import settings


def get_full_program_data(
    checking_key: Literal['is_took'] | Literal['has_limit'],
    time_type: Literal['took_time'] | Literal['changed_time']
) -> list:
    data = _get_data()
    return _get_program_data(data, checking_key, time_type)


def _get_data() -> dict:
    response = httpx.get(f'{settings.LIMIT_PARSER_HOST}/api/fuelcards/')
    return response.json()


def _get_program_data(
    received_data: dict,
    checking_key: Literal['is_took'] | Literal['has_limit'],
    time_type: Literal['took_time'] | Literal['changed_time']
) -> list:
    report_data = []
    for card_data in received_data:
        if card_data.get(checking_key):
            date, time = dt.get_date_and_time(card_data[time_type])
            data = [date, time, card_data['number'], card_data['limit']]
            report_data.append(data)
    return report_data
