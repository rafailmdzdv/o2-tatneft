import time

import httpx

from models.card import Card
from settings import config
from settings.log import logger as log


def main():
    while True:
        card = _try_get_random_card()
        _try_send_card_number(card)
        time.sleep(config.MINUTES_IN_SECONDS)


def _try_get_random_card() -> Card:
    try:
        return _get_random_card()
    except Exception as _ex:
        log.error(f'Cannot get random card -> {_ex}')
        raise


def _get_random_card() -> Card:
    response = httpx.get(f'{config.API_URL_PREFIX}/random/')
    return Card.parse_obj(response.json())


def _try_send_card_number(card: Card) -> None:
    try:
        response = _send_card_number(card)
        log.debug(f'Card sent successfully\nMessage from server -> {response}')
    except Exception as _ex:
        log.error(f'Cannot send card number -> {_ex}')
        raise


def _send_card_number(card: Card) -> dict:
    response = httpx.put(f'{config.API_URL_PREFIX}/send_card/{card.number}/')
    return response.json()


if __name__ == '__main__':
    main()
