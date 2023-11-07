from helpers import BasePage


class AllPromotionsPage(BasePage):
    PRODUCT_LOCATOR = "//*[contains(text(),'Строительная')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_product_locator(self):
        self.click_on(self.PRODUCT_LOCATOR)