from selenium.webdriver.common.by import By

from helpers import BasePage
from elements import HeaderElement
from data.urls import TIRES_PAGE_URL


class TiresPage(BasePage):
    text_tires_title = "//h1[@class='content__header cr-category_header']"
    PRICE_MIN_LOCATOR = "//input[@name='filter[price][from]']"
    PRICE_MAX_LOCATOR = "//input[@name='filter[price][to]']"
    TIRE_BRAND_LOCATOR = "//select[@id='brand']"
    AUDI_LOCATOR = "//option[@value='Audi']"
    MODEL_LOCATOR = "//select[@id='model']"
    MODEL_100_LOCATOR = "//option[@value='100']"
    YEAR_OF_ISSUE = "//select[@id='year']"
    YEAR_1968_ISSUE = "//option[@value='1968']"
    MODIFICATION_LOCATOR = "//select[@id='modification']"
    SHOW_BUTTON = "//button[@name='filter[sa]']"
    RESULT_INNER = "//div[@class='b-result g-box_lseparator']"
    TO_ORDER_LOCATOR = "//label[@title='Под заказ']"
    text_to_order = "//*[contains(text(),'Под заказ')]"

    def open(self):
        self.driver.get(TIRES_PAGE_URL)

    def assert_text_in_button_and_title_of_page_tires(self):
        actual_text = self.driver.find_element(By.XPATH, HeaderElement.TIRES_LOCATOR).text
        text_in_button = self.driver.find_element(By.XPATH, self.text_tires_title).text
        assert actual_text in text_in_button

    def click_on_min_price(self):
        self.wait_for_visible(self.PRICE_MIN_LOCATOR)
        self.click_on(self.PRICE_MIN_LOCATOR)

    def click_on_max_price(self):
        self.wait_for_visible(self.PRICE_MAX_LOCATOR)
        self.click_on(self.PRICE_MAX_LOCATOR)

    def input_uncorrect_min_price(self):
        self.fill(self.PRICE_MIN_LOCATOR, 5)

    def input_uncorrect_max_price(self):
        self.fill(self.PRICE_MAX_LOCATOR, 5)

    def click_on_all_button_in_section_selection_by_car(self):
        self.wait_for_visible(self.TIRE_BRAND_LOCATOR)
        self.click_on(self.TIRE_BRAND_LOCATOR)
        self.click_on(self.AUDI_LOCATOR)
        self.click_on(self.MODEL_LOCATOR)
        self.click_on(self.MODEL_100_LOCATOR)
        self.click_on(self.YEAR_OF_ISSUE)
        self.click_on(self.YEAR_1968_ISSUE)

    def assert_result_inner(self):
        text_in_button = self.driver.find_element(By.XPATH, self.SHOW_BUTTON).text
        assert "(" in text_in_button

    def assert_automatic_correction_of_incorrect_min_price(self):
        self.wait_for_visible(self.PRICE_MIN_LOCATOR)
        price_in_button = self.driver.find_element(By.XPATH, self.PRICE_MIN_LOCATOR).get_attribute("value")
        assert price_in_button == "71", "Automatic playback of minimum price did not work"

    def assert_automatic_correction_of_incorrect_max_price(self):
        self.wait_for_visible(self.PRICE_MAX_LOCATOR)
        price_in_button = self.driver.find_element(By.XPATH, self.PRICE_MAX_LOCATOR).get_attribute("value")
        assert price_in_button == "72", "Automatic playback of minimum price did not work"

    def click_on_to_order_locator(self):
        self.wait_for_visible(self.TO_ORDER_LOCATOR)
        self.click_on(self.TO_ORDER_LOCATOR)

    def click_on_show_button(self):
        self.click_on(self.SHOW_BUTTON)

    def assert_scroll_to_order_checkbox(self):
        self.assert_scroll_to_element(self.TO_ORDER_LOCATOR)

    def assert_text_after_click_to_order_button(self):
        text = "заказ"
        text_in_checkbox = self.driver.find_element(By.XPATH, self.text_to_order).text
        assert text in text_in_checkbox