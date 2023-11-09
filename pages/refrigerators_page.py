import allure

from selenium.webdriver.common.by import By
from elements import HeaderElement
from helpers import BasePage


class RefrigeratorsPage(BasePage):
    text_refrigerators_locator = "//h1[@class='style_title__1u7Nj']"
    PRICE_MIN_LOCATOR = "//input[@id='minPrice']"
    PRICE_MAX_LOCATOR = "//input[@id='maxPrice']"

    @allure.step("Assert text in button and title refrigerators")
    def assert_text_in_button_and_title_of_page_refrigerators(self):
        actual_text = self.driver.find_element(By.XPATH, HeaderElement.REFRIGERATORS_LOCATOR).text
        text_in_button = self.driver.find_element(By.XPATH, self.text_refrigerators_locator).text
        assert actual_text in text_in_button

    @allure.step("Click on minimal price")
    def click_on_min_price(self):
        self.click_on(self.PRICE_MIN_LOCATOR)

    @allure.step("Click on max price")
    def click_on_max_price(self):
        self.click_on(self.PRICE_MAX_LOCATOR)

    @allure.step("Input uncorrect min price")
    def input_uncorrect_min_price(self):
        self.fill(self.PRICE_MIN_LOCATOR, 5)

    @allure.step("Assert automatic correction of incorrect min price")
    def assert_automatic_correction_of_incorrect_min_price(self):
        self.wait_for_visible(self.PRICE_MIN_LOCATOR)
        price_in_button = self.driver.find_element(By.XPATH, self.PRICE_MIN_LOCATOR).get_attribute("value")
        assert price_in_button == "83,72", "Automatic playback of minimum price did not work"