import allure

from elements import HeaderElement
from pages import RefrigeratorsPage


@allure.feature("Refrigerators")
@allure.story("Check refrigerators text")
@allure.severity('normal')
def test_check_refrigerators_button(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.click_on_refrigerators_locator()

    refrigerators_page = RefrigeratorsPage(driver)
    refrigerators_page.assert_text_in_button_and_title_of_page_refrigerators()


@allure.feature("Refrigerators")
@allure.story("Check Minimum Price")
@allure.severity('normal')
def test_check_min_price(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.click_on_refrigerators_locator()

    tires_page = RefrigeratorsPage(driver)
    tires_page.click_on_min_price()
    tires_page.input_uncorrect_min_price()
    tires_page.click_on_max_price()
    tires_page.assert_automatic_correction_of_incorrect_min_price()


@allure.feature("Refrigerators")
@allure.story("Check choose manufacturer in sorting settings")
@allure.severity('normal')
def test_choose_manufacturer(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.click_on_refrigerators_locator()

    refrigerators_page = RefrigeratorsPage(driver)
    refrigerators_page.click_on_atlant_checkbox()
    refrigerators_page.click_on_apply_button()
    refrigerators_page.assert_sorting_manufacturer()


@allure.feature("Refrigerators")
@allure.story("Check correct work one chamber button")
@allure.severity('normal')
def test_one_chamber_button(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.click_on_refrigerators_locator()

    refrigerators_page = RefrigeratorsPage(driver)
    refrigerators_page.click_on_one_chamber_button()
    refrigerators_page.assert_text_in_one_chamber_title()


@allure.feature("Refrigerators")
@allure.story("Check correct work two chamber button")
@allure.severity('normal')
def test_two_chamber_button(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.click_on_refrigerators_locator()

    refrigerators_page = RefrigeratorsPage(driver)
    refrigerators_page.click_on_two_chamber_button()
    refrigerators_page.assert_text_in_two_chamber_title()


@allure.feature("Sort reset")
@allure.story("Changing sorting settings on the refrigerators page")
@allure.severity('normal')
def test_sort_reset_button(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.click_on_refrigerators_locator()

    refrigerators_page = RefrigeratorsPage(driver)
    refrigerators_page.click_on_atlant_checkbox()
    refrigerators_page.assert_displayed_of_sort_reset()