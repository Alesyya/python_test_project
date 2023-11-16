import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from data import DOMAIN
from helpers import BasePage


class MainPage(BasePage):
    COOKIE_LOCATOR = "//div[@class='AgreementCookie_modal__x3nra']//div[contains(text(),'Принять')]"
    ADD_TO_BASKET_LOCATOR = "//div[@data-testid='card-343550']//div[@class='ProductHome_actions___ekjB']"
    PRODUCT_WITH_SALE_BUTTON_LOCATOR = "//span[contains(text(),'Товары со скидкой')]"
    SALE_LOCATOR = "//div[contains(@class,'EntitiesList_content__Mymfq')]//*[contains(text(),'%')]"
    PRODUCT_WITH_PRESENT_BUTTON_LOCATOR = "//span[contains(text(),'Товары с подарками')]"
    PRESENT_LOCATOR = "//*[contains(text(),'+ Подарок')]"
    SUPER_PRICE_BUTTON_LOCATOR = "//span[contains(text(),'Суперцена')]"
    SUPER_PRICE_LOCATOR = "//div[contains(@class,'EntitiesList_content__Mymfq')]//*[contains(text(),'Суперцена')]"
    DISCOUNTED_PRODUCT_BUTTON_LOCATOR = "//span[contains(text(),'Уцененные товары')]"
    DISCOUNTED_PRODUCT_LOCATOR = "//*[contains(text(),'Уцененный товар')]"

    @allure.step("Open the website")
    def open(self):
        self.driver.get(DOMAIN)

    @allure.step("Click add to basket product")
    def click_product_to_basket_button(self):
        self.wait_for_visible(self.ADD_TO_BASKET_LOCATOR)
        self.click_on(self.ADD_TO_BASKET_LOCATOR)

    @allure.step("Click on product with sale button")
    def click_on_product_with_sale_button(self):
        self.click_on(self.PRODUCT_WITH_SALE_BUTTON_LOCATOR)

    @allure.step("Click on product with surprise button")
    def click_on_product_with_surprise_button(self):
        self.click_on(self.PRODUCT_WITH_PRESENT_BUTTON_LOCATOR)

    @allure.step("Click on super price button")
    def click_on_super_price_button(self):
        self.click_on(self.SUPER_PRICE_BUTTON_LOCATOR)

    @allure.step("Click on discounted product button")
    def click_on_discounted_product_button(self):
        self.click_on(self.DISCOUNTED_PRODUCT_BUTTON_LOCATOR)

    @allure.step("Click on accept cookies")
    def accept_cookies(self):
        WebDriverWait(self.driver, self.WAIT_UNTIL).until(EC.visibility_of_element_located((By.XPATH,
                                                                                            self.COOKIE_LOCATOR)))
        self.click_on(self.COOKIE_LOCATOR)

    @allure.step("Assert title main page")
    def assert_main_page_title(self):
        assert self.driver.title == "Онлайн-гипермаркет 21vek.by"

    @allure.step("Assert visible persent of sale")
    def assert_visible_persent_of_sale_text(self):
        self.assert_element_is_present(self.SALE_LOCATOR)

    @allure.step("Assert visible present text")
    def assert_visible_present_text(self):
        self.assert_element_is_present(self.PRESENT_LOCATOR)

    @allure.step("Assert visible super price text")
    def assert_visible_super_price_text(self):
        self.assert_element_is_present(self.SUPER_PRICE_LOCATOR)

    @allure.step("Assert visible discounted product text")
    def assert_visible_discounted_product_text(self):
        self.assert_element_is_present(self.DISCOUNTED_PRODUCT_LOCATOR)