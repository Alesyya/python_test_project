import allure

from selenium.webdriver.common.by import By

from data import DOMAIN
from helpers import BasePage


class HeaderElement(BasePage):
    LOGO_LOCATOR = "//a[@class='logotypeImg']"
    ALL_PROMOTION_LOCATOR = "//div[@class='styles_promoItem__aolWq']//a[@href='/special_offers/promo.html']"
    CITY_LOCATOR = "//button[@type='button' and @class='styles_localityBtn__qrGFQ']"
    ACCOUNT_LOCATOR = "//span[@class='userToolsText']"
    POPULATED_PLACE_LOCATOR = "//input[@label='Населенный пункт']"
    BUTON_CLOSE_LOCATOR = "//button[@type='button' and @tabindex='-1' and @class='style_clearBtn__OGU2X']"
    SELECT_CITY_FROM_LIST_LOCATOR = "//li[@role = 'row']/div[text() = 'Гродно']"
    SAVE_BUTTON_LOCATOR = "//div[@class='Button-module__buttonText' and text()='Сохранить']"
    CHOOSE_CITY_LOCATOR = "//button[contains(text(),'Гродно')]"
    MARKDOWN_LOCATOR = "//a[@href='/special_offers/promo.html?discountTypes=sale']"
    REFRIGERATORS_LOCATOR = "//a[@href='/refrigerators/']"
    TIRES_LOCATOR = "//a[@href='/tires/']"
    WASHING_MACHINES = "//a[@href='/washing_machines/']"
    BOILERS_LOCATOR = "//a[@href='/boilers/']"
    PHONES_LOCATOR = "//a[@href='/mobile/']"
    NOTEBOOKS_LOCATOR = "//a[@href='/notebooks/']"
    TV_LOCATOR = "//a[@href='/tv/']"
    VAKUUM_LOCATOR = "//a[@href='/vacuum/']"
    MATTRESS_LOCATOR = "//a[@href='/mattresses/']"
    SOFA_LOCATOR = "//a[@href='/cushioned_furniture/']"
    BASKET_LOCATOR = "//div[@class='headerCart']"
    ERROR_ICON_INCORRECT_INPUT_COUNTRY = "//span[@class='input-error-message__icon-wrapper']"

    @allure.step("Open the website")
    def open(self):
        self.driver.get(DOMAIN)

    @allure.step("Click on city choose")
    def click_on_city_locator(self):
        self.click_on(self.CITY_LOCATOR)

    @allure.step("Click on all promotion")
    def click_on_all_promotions_locator(self):
        self.click_on(self.ALL_PROMOTION_LOCATOR)

    @allure.step("Click on account button")
    def click_on_account_locator(self):
        self.wait_for_visible(self.LOGO_LOCATOR)
        self.click_on(self.ACCOUNT_LOCATOR)

    @allure.step("Click on close button")
    def click_on_but_close_locator(self):
        self.click_on(self.BUTON_CLOSE_LOCATOR)

    @allure.step("Click on select city from list")
    def click_on_select_city_from_list(self):
        self.click_on(self.SELECT_CITY_FROM_LIST_LOCATOR)

    @allure.step("Click on save button")
    def click_on_save_button_locator(self):
        self.click_on(self.SAVE_BUTTON_LOCATOR)

    @allure.step("Click on refrigerators")
    def click_on_refrigerators_locator(self):
        self.click_on(self.REFRIGERATORS_LOCATOR)

    @allure.step("Click on tires")
    def click_on_tires_locator(self):
        self.click_on(self.TIRES_LOCATOR)

    @allure.step("Click on phones")
    def click_on_phones_locator(self):
        self.click_on(self.PHONES_LOCATOR)

    @allure.step("Click on tv")
    def click_on_tv_locator(self):
        self.click_on(self.TV_LOCATOR)

    @allure.step("Click on basket")
    def click_on_basket(self):
        self.click_on(self.BASKET_LOCATOR)

    @allure.step("Fill country field")
    def fill_country_field(self):
        self.fill(self.POPULATED_PLACE_LOCATOR, "Мальта")

    @allure.step("Assert choose country correct")
    def assert_choose_country(self):
        assert self.driver.find_element(By.XPATH, self.CHOOSE_CITY_LOCATOR).text == 'г. Гродно'

    @allure.step("Assert visible logo")
    def assert_visible_logo(self):
        self.assert_element_is_present(self.LOGO_LOCATOR)

    @allure.step("Assert correct visible product text")
    def assert_correct_visible_text_product(self):
        self.assert_text_in_element(self.ALL_PROMOTION_LOCATOR, "Все акции")
        self.assert_text_in_element(self.MARKDOWN_LOCATOR, "Уценка")
        self.assert_text_in_element(self.REFRIGERATORS_LOCATOR, "Холодильники")
        self.assert_text_in_element(self.TIRES_LOCATOR, "Шины")
        self.assert_text_in_element(self.WASHING_MACHINES, "Стиральные машины")
        self.assert_text_in_element(self.BOILERS_LOCATOR, "Котлы")
        self.assert_text_in_element(self.PHONES_LOCATOR, "Смартфоны")
        self.assert_text_in_element(self.NOTEBOOKS_LOCATOR, "Ноутбуки")
        self.assert_text_in_element(self.TV_LOCATOR, "Телевизоры")
        self.assert_text_in_element(self.VAKUUM_LOCATOR, "Пылесосы")
        self.assert_text_in_element(self.MATTRESS_LOCATOR, "Матрасы")
        self.assert_text_in_element(self.SOFA_LOCATOR, "Диваны")

    @allure.step("Assert incorrect input country")
    def assert_incorrect_input_country(self):
        self.assert_element_is_displayed(self.ERROR_ICON_INCORRECT_INPUT_COUNTRY)






