import re
from selenium.webdriver.common.by import By
from helpers import BasePage


class BuildingBoardProductPage(BasePage):
    PRICE_WITH_DISCOUNT_LOCATOR = "//span[@data-code='6241841' and @data-producer_name]"
    PRICE_WITHOUT_DISCOUNT_LOCATOR = "//span[@class=' g-price g-oldprice item__oldprice']"
    ADD_TO_FAVORITES_LOCATOR = "//span[@class=' g-pseudo_href']"
    DELETE_FROM_FAVORITES_LOCATOR = "//span[contains(text(),'Удалить из избранного')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_sale(self):
        higher_price1 = self.driver.find_element(By.XPATH, self.PRICE_WITHOUT_DISCOUNT_LOCATOR)
        lower_price2 = self.driver.find_element(By.XPATH, self.PRICE_WITH_DISCOUNT_LOCATOR)
        higher_price = float(re.sub('[^0-9.]', '', higher_price1.text))
        lower_price = float(re.sub('[^0-9.]', '', lower_price2.text))

        if higher_price > lower_price:
            print("Цена снижена")
        elif higher_price < lower_price:
            print("Цена не снижена")
        else:
            print("Цены равны")

    def click_on_favorites_locator(self):
        self.click_on(self.ADD_TO_FAVORITES_LOCATOR)

    def checking_product_is_in_favorites(self):
        assert self.driver.find_element(By.XPATH, self.DELETE_FROM_FAVORITES_LOCATOR).text == "Удалить из избранного"