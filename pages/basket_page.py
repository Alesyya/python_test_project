from selenium.webdriver.common.by import By
from helpers import BasePage


class BasketPage(BasePage):
    NUMBERS_ITEMS_IN_BASKET = "//span[@class='BasketTabsScreen_counter___R5Jp']"
    BASKET_LOCATOR = "//div[@class='headerCart']"
    ADD_TO_BASKET_LOCATOR = "//div[@data-testid='card-343550']//div[@class='ProductHome_actions___ekjB']"
    DELETE_LOCATOR = "//button[@class='styles_reactButton__ArODZ styles_inline__ilTcV']"
    CONFIRM_DELETE_LOCATOR = "//div[@class='Button-module__buttonText' and text()='Удалить']"
    MESSAGE_DELETE_PRODUCT_LOCATOR = "//div[@id='react-popover']"
    ADD_TO_FAVORITES_LOCATOR = "//button[@class='styles_reactButton__ArODZ ButtonsBlock_favButton__vhlam styles_inline__ilTcV']"
    PLUS_LOCATOR = "//*[@class='Counter_counter__ftQCi BasketItem_counter__wv8ja']//*[@fill-rule='evenodd']"
    COUNT_PRODUCT_LOCATOR = "//input[@class='Counter_counterInput__idJlc BasketItem_counterInput__qzSqN']"
    ADD_ADDITIONAL_SERVICE_LOCATOR = "//div[contains(@class, 'styles_checkbox__2ZkYB ')]"
    COUNT_ADDITIONAL_SERVICE_LOCATOR = "//span[contains(text(),'Услуги')]"
    MESSAGE_DELETE_ADDITIONAL_SERVICE_LOCATOR = "//div[contains(text(),'Услуга удалена')]"

    def open(self):
        self.driver.get('https://www.21vek.by/order/')

    def click_on_basket(self):
        self.wait_for_visible(self.BASKET_LOCATOR)
        self.click_on(self.BASKET_LOCATOR)

    def click_product_to_basket_locator(self):
        self.assert_scroll_to_element(self.ADD_TO_BASKET_LOCATOR)
        self.click_on(self.ADD_TO_BASKET_LOCATOR)

    def click_on_delete_from_basket_locator(self):
        self.click_on(self.DELETE_LOCATOR)

    def click_on_confirm_delete_locator(self):
        self.click_on(self.CONFIRM_DELETE_LOCATOR)

    def click_on_add_to_favorites(self):
        self.wait_for_visible(self.ADD_TO_FAVORITES_LOCATOR)
        self.click_on(self.ADD_TO_FAVORITES_LOCATOR)

    def click_on_plus_locator(self):
        # self.wait_for_visible(self.PLUS_LOCATOR)
        self.click_on(self.PLUS_LOCATOR)

    def click_on_additional_service_locator(self):
        self.click_on(self.ADD_ADDITIONAL_SERVICE_LOCATOR)

    def assert_items_is_add_to_basket(self):
        self.wait_for_visible(self.NUMBERS_ITEMS_IN_BASKET)
        text_in_button = self.driver.find_element(By.XPATH, self.NUMBERS_ITEMS_IN_BASKET).text
        assert "1" in text_in_button

    def assert_text_succsses_delete_product(self):
        self.assert_text_in_element(self.MESSAGE_DELETE_PRODUCT_LOCATOR, 'Товар удален из корзины')

    def assert_text_succsses_add_to_favorites(self):
        self.assert_text_in_element(self.ADD_TO_FAVORITES_LOCATOR, 'В избранном')

    def assert_text_add_count_product(self):
        self.assert_text_get_value(self.COUNT_PRODUCT_LOCATOR, '2')

    def assert_count_additional_service(self):
        text_in_button = self.driver.find_element(By.XPATH, self.COUNT_ADDITIONAL_SERVICE_LOCATOR).text
        assert "Услуги" in text_in_button

    def assert_delete_additional_service(self):
        self.assert_text_in_element(self.MESSAGE_DELETE_ADDITIONAL_SERVICE_LOCATOR, 'Услуга удалена')

    def add_to_basket(self):
        self.click_product_to_basket_locator()
        self.click_on_basket()

    def add_additional_service(self):
        self.click_on_additional_service_locator()