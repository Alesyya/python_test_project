import allure

from elements import HeaderElement
from pages import TiresPage


@allure.feature("Refrigerators")
@allure.story("Check refrigerators text")
@allure.severity('normal')
def test_сlick_on_the_opening_page_tires_open_tires(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.click_on_tires_locator()

    tires_page = TiresPage(driver)
    tires_page.assert_text_in_button_and_title_of_page_tires()


@allure.feature("Price")
@allure.story("Check input min price")
@allure.severity('normal')
def test_min_price(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.click_on_tires_locator()

    tires_page = TiresPage(driver)
    tires_page.click_on_min_price()
    tires_page.input_uncorrect_min_price()
    tires_page.click_on_max_price()
    tires_page.assert_automatic_correction_of_incorrect_min_price()


@allure.feature("Price")
@allure.story("Check input max price")
@allure.severity('normal')
def test_max_price(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.click_on_tires_locator()

    tires_page = TiresPage(driver)
    tires_page.click_on_max_price()
    tires_page.input_uncorrect_max_price()
    tires_page.click_on_min_price()
    tires_page.assert_automatic_correction_of_incorrect_max_price()


@allure.feature("Section selection")
@allure.story("Check work checkbox in section selection")
@allure.severity('normal')
def test_section_selection_by_car(driver, accept_cookies):
    tires_page = TiresPage(driver)
    tires_page.open()
    tires_page.click_on_all_button_in_section_selection_by_car()
    tires_page.assert_result_inner()


@allure.feature("Order")
@allure.story("Check order tires")
@allure.severity('normal')
def test_to_order_tires(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.click_on_tires_locator()

    tires_page = TiresPage(driver)
    tires_page.scroll_to_order_checkbox()
    tires_page.click_on_to_order_locator()
    tires_page.click_on_show_button()
    tires_page.assert_text_after_click_to_order_button()