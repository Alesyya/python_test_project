import allure

from selenium.webdriver.common.by import By
from elements import HeaderElement
from helpers import BasePage


class RefrigeratorsPage(BasePage):
    APPLY_BUTTON_LOCATOR = "//div[text()='Применить фильтр']"
    text_refrigerators_locator = "//h1[@class='style_title__1u7Nj']"
    PRICE_MIN_LOCATOR = "//input[@id='minPrice']"
    PRICE_MAX_LOCATOR = "//input[@id='maxPrice']"
    ATLANT_CHECKBOX_LOCATOR = "//button[@data-testid='producer-atlant']//div[@class='styles_checkbox__18jKd']"
    product_text_locator = "//p[@class='CardInfo_info__2XVo8 style_fullNameContainer__3kd0q']"
    ONE_CHAMBER_BUTTON_LOCATOR = "//a[text()='Однокамерные']"
    text_title_one_chamber_locator = "//h1[text()='Холодильники однокамерные']"
    TWO_CHAMBER_LOCATOR = "//a[text()='Двухкамерные']"
    text_title_two_chamber_locator = "//h1[text()='Холодильники двухкамерные']"
    SORT_RESET_BUTTON_LOCATOR = "//div[@class='style_applyButtonWrapper__1esCD']//span"

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

    @allure.step("Click on atlant checkbox")
    def click_on_atlant_checkbox(self):
        self.scroll_to_element(self.ATLANT_CHECKBOX_LOCATOR)
        self.click_on(self.ATLANT_CHECKBOX_LOCATOR)

    @allure.step("Click on apply button")
    def click_on_apply_button(self):
        self.click_on(self.APPLY_BUTTON_LOCATOR)

    @allure.step("Assert automatic correction of incorrect min price")
    def assert_sorting_manufacturer(self):
        text_in_button = self.driver.find_element(By.XPATH, self.product_text_locator).text
        assert "ATLANT" in text_in_button

    @allure.step("Click on one chamber button")
    def click_on_one_chamber_button(self):
        self.click_on(self.ONE_CHAMBER_BUTTON_LOCATOR)

    @allure.step("Assert text in one chamber title")
    def assert_text_in_one_chamber_title(self):
        text_in_button = self.driver.find_element(By.XPATH, self.text_title_one_chamber_locator).text
        assert "однокамерные" in text_in_button

    @allure.step("Click on two chamber button")
    def click_on_two_chamber_button(self):
        self.click_on(self.TWO_CHAMBER_LOCATOR)

    @allure.step("Assert text in two chamber title")
    def assert_text_in_two_chamber_title(self):
        text_in_button = self.driver.find_element(By.XPATH, self.text_title_two_chamber_locator).text
        assert "двухкамерные" in text_in_button

    @allure.step("Assert displayed of sort reset")
    def assert_displayed_of_sort_reset(self):
        self.assert_element_is_displayed(self.SORT_RESET_BUTTON_LOCATOR)
