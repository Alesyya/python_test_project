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

    def open(self):
        self.driver.get(DOMAIN)

    def click_product_to_basket_button(self):
        self.wait_for_visible(self.ADD_TO_BASKET_LOCATOR)
        self.click_on(self.ADD_TO_BASKET_LOCATOR)

    def click_on_product_with_sale_button(self):
        self.click_on(self.PRODUCT_WITH_SALE_BUTTON_LOCATOR)

    def click_on_product_with_surprise_button(self):
        self.click_on(self.PRODUCT_WITH_PRESENT_BUTTON_LOCATOR)

    def click_on_super_price_button(self):
        self.click_on(self.SUPER_PRICE_BUTTON_LOCATOR)

    def click_on_discounted_product_button(self):
        self.click_on(self.DISCOUNTED_PRODUCT_BUTTON_LOCATOR)

    def accept_cookies(self):
        WebDriverWait(self.driver, self.WAIT_UNTIL).until(EC.visibility_of_element_located((By.XPATH,
                                                                                            self.COOKIE_LOCATOR)))
        self.click_on(self.COOKIE_LOCATOR)

    def assert_main_page_title(self):
        assert self.driver.title == "Онлайн-гипермаркет 21vek.by"

    def assert_visible_persent_of_sale_text(self):
        self.assert_element_is_present(self.SALE_LOCATOR)

    def assert_visible_present_text(self):
        self.assert_element_is_present(self.PRESENT_LOCATOR)

    def assert_visible_super_price_text(self):
        self.assert_element_is_present(self.SUPER_PRICE_LOCATOR)

    def assert_visible_discounted_product_text(self):
        self.assert_element_is_present(self.DISCOUNTED_PRODUCT_LOCATOR)