from elements.footer_element import FooterElement
from data import (VIBER_PAGE_URL, TELEGRAM_PAGE_URL, VK_PAGE_URL, FACEBOOK_PAGE_URL, YOUTUBE_PAGE_URL, YANDEX_PAGE_URL)


def test_check_viber_page(driver, accept_cookies):
    footer_element = FooterElement(driver)
    footer_element.open()
    footer_element.click_on_viber_locator()
    footer_element.switch_between_windows()
    footer_element.assert_actual_url(VIBER_PAGE_URL)


def test_check_telegram_page(driver, accept_cookies):
    footer_element = FooterElement(driver)
    footer_element.open()
    footer_element.click_on_telegram_locator()
    footer_element.switch_between_windows()
    footer_element.assert_actual_url(TELEGRAM_PAGE_URL)


def test_check_vk_page(driver, accept_cookies):
    footer_element = FooterElement(driver)
    footer_element.open()
    footer_element.click_on_vk_locator()
    footer_element.switch_between_windows()
    footer_element.assert_actual_url(VK_PAGE_URL)


def test_check_facebook_page(driver, accept_cookies):
    footer_element = FooterElement(driver)
    footer_element.open()
    footer_element.click_on_facebook_locator()
    footer_element.switch_between_windows()
    footer_element.assert_actual_url(FACEBOOK_PAGE_URL)


def test_check_youtube_page(driver, accept_cookies):
    footer_element = FooterElement(driver)
    footer_element.open()
    footer_element.click_on_youtube_locator()
    footer_element.switch_between_windows()
    footer_element.assert_actual_url(YOUTUBE_PAGE_URL)


def test_check_zen_yandex_page(driver, accept_cookies):
    footer_element = FooterElement(driver)
    footer_element.open()
    footer_element.click_on_zen_yandex_locator()
    footer_element.switch_between_windows()
    footer_element.assert_actual_url(YANDEX_PAGE_URL)


def test_check_form_write_to_us(driver, accept_cookies):
    footer_element = FooterElement(driver)
    footer_element.open()
    footer_element.click_on_write_us_locator()
    footer_element.fill_form_write_us()