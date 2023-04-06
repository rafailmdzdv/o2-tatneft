from datetime import datetime

from playwright.sync_api import (Browser,
                                 ElementHandle,
                                 Page,
                                 sync_playwright)

from app import models
from project_config.envs import env
from project_config.log import logger as log


def start_adding_limit_and_update_data(card_number: str) -> None:
    _start_adding_limit(card_number)
    card = models.FuelCard.objects.get(number=card_number)
    _update_card_data(card)


def _start_adding_limit(card_number: str) -> None:
    with sync_playwright() as sp:
        browser = sp.chromium.launch(headless=False)
        lk_page = _authorize_to_lk(browser)
        card_page = _find_card_in_cards_page(lk_page, card_number)
        _add_limit(card_page)
        log.debug(f'Successfully added limit to {card_number}')
        card_page.wait_for_timeout(1000)
        browser.close()


def _authorize_to_lk(browser: Browser) -> Page:
    signin_page = _open_signin_page(browser)
    signin_page.wait_for_selector('#slqusername').fill(env.LK_TATNEFT_LOGIN)
    signin_page.wait_for_selector('#slqpassword').fill(env.LK_TATNEFT_PASSWORD)
    signin_page.wait_for_selector('[type="submit"]').click()
    return signin_page


def _open_signin_page(browser: Browser) -> Page:
    page = browser.new_page()
    page.goto('http://lk-demo.tatneft.ru/')
    return page


def _find_card_in_cards_page(page: Page, card_number: str) -> Page:
    cards_page = _open_cards_page(page)
    return _find_card(cards_page, card_number)


def _open_cards_page(page: Page) -> Page:
    page.wait_for_timeout(500)
    page.goto(page.url.replace('main', 'cards'))
    return page


def _find_card(cards_page: Page, card_number: str) -> Page:
    cards_page.wait_for_selector('[placeholder="Номер карты"]').fill(card_number)
    cards_page.keyboard.press('Enter')
    divided_card_number = _divide_card_number(card_number)
    cards_page.wait_for_timeout(1000)
    cards_page.wait_for_selector(f'text={divided_card_number}').click()
    return cards_page


def _divide_card_number(card_number: str) -> str:
    divided_card_number = ''
    divide_index = 4
    for index, char in enumerate(card_number, start=1):
        divided_card_number += char
        if not index % divide_index:
            divided_card_number += ' '
            divide_index += 4
    return divided_card_number


def _add_limit(card_page: Page) -> None:
    card_page.wait_for_selector('text=Добавить лимит').click()
    limit_form = card_page.wait_for_selector('mat-dialog-container')
    card_page.wait_for_timeout(500)

    _select_category(limit_form, card_page)  # type: ignore
    _select_group(limit_form, card_page)  # type: ignore
    _select_limit_type(limit_form, card_page)  # type: ignore
    _input_max_value(limit_form)  # type: ignore

    limit_form.wait_for_selector('text=Сохранить').click()


def _select_category(limit_form: ElementHandle, card_page: Page) -> None:
    category_list = limit_form.query_selector_all('mat-form-field')[0]
    category_list.click()
    card_page.wait_for_selector('#cdk-overlay-1')\
        .wait_for_selector('text=ДТЗ').click()


def _select_group(limit_form: ElementHandle, card_page: Page) -> None:
    group_list = limit_form.query_selector_all('mat-form-field')[1]
    group_list.click()
    card_page.wait_for_selector('#cdk-overlay-2')\
        .wait_for_selector('text=Летнее').click()


def _select_limit_type(limit_form: ElementHandle, card_page: Page) -> None:
    limit_type_box = limit_form.query_selector_all('mat-form-field')[3]
    limit_type_box.click()
    card_page.wait_for_selector('#cdk-overlay-3')\
        .wait_for_selector('text=Разрешено в заданных пределах').click()


def _input_max_value(limit_form: ElementHandle) -> None:
    max_value_input = limit_form.query_selector_all('input')[0]
    max_value_input.fill('600')


def _update_card_data(card: models.FuelCard):
    card.has_limit = True
    card.changed_time = datetime.now()
    card.limit = 600
    card.save()
