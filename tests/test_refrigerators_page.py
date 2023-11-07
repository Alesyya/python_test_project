from elements import HeaderElement
from pages import RefrigeratorsPage


def test_check_refrigerators_button(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.click_on_refrigerators_locator()

    refrigerators_page = RefrigeratorsPage(driver)
    refrigerators_page.assert_text_in_button_and_title_of_page_refrigerators()


def test_check_min_price(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.click_on_refrigerators_locator()

    tires_page = RefrigeratorsPage(driver)
    tires_page.click_on_min_price()
    tires_page.input_uncorrect_min_price()
    tires_page.click_on_max_price()
    tires_page.assert_automatic_correction_of_incorrect_min_price()