from data import DOMAIN
from helpers import BasePage
from data.users import USER_AlESYA


class FooterElement(BasePage):
    VIBER_LOCATOR = "//a[@class='Contacts_contactsBlockItem__Q_Lbt Contacts_viber__7S_zO']"
    TELEGRAM_LOCATOR = "//div[@id='footer']//a[@href='http://t.me/e21vekbot']"
    EMAIL_LOCATOR = "//div[@id='footer']//a[@href='mailto:21@21vek.by']"
    VK_LOCATOR = "//div[@id='footer']//a[@href='https://vk.com/21vek_by']"
    FACEBOOK_LOCATOR = "//div[@id='footer']//a[@href='https://www.facebook.com/21vek.by/']"
    YOUTUBE_LOCATOR = "//div[@id='footer']//a[@href='https://www.youtube.com/channel/UChNfLMJmxWcaMy1oPxxSvog']"
    ZEN_YANDEX_LOCATOR = "//div[@id='footer']//a[@href='https://zen.yandex.ru/id/5e4f94ae386b1c555647f49a']"
    WRITE_US_LOCATOR = "//button[@class='Contacts_contactsBlockItem__Q_Lbt Contacts_feedback__eiVnQ']"
    NAME_LOCATOR = "//input[@label='Имя']"
    EMAIL_WRITE_US_LOCATOR = "//input[@label='Электронная почта или номер телефона']"
    MASSAGE_INPUT_LOCATOR = "//textarea[@class='BaseTextArea-module__input']"
    ACSSEPT_LOCATOR = "//span[@class='SvgIcon-module__base BaseCheckBox-module__uncheckedIcon styles-module__icon16']"
    SEND_LOCATOR = "//div[text()='Отправить']"
    TEXT_LOCATOR = "//h5[@class='styles_successTitle__YoP7v']"

    def open(self):
        self.driver.get(DOMAIN)

    def click_on_viber_locator(self):
        self.wait_for_visible(self.VIBER_LOCATOR)
        self.click_on(self.VIBER_LOCATOR)

    def click_on_telegram_locator(self):
        self.click_on(self.TELEGRAM_LOCATOR)

    def click_on_email_locator(self):
        self.click_on(self.EMAIL_LOCATOR)

    def click_on_vk_locator(self):
        self.click_on(self.VK_LOCATOR)

    def click_on_facebook_locator(self):
        self.click_on(self.FACEBOOK_LOCATOR)

    def click_on_youtube_locator(self):
        self.click_on(self.YOUTUBE_LOCATOR)

    def click_on_zen_yandex_locator(self):
        self.click_on(self.ZEN_YANDEX_LOCATOR)

    def click_on_write_us_locator(self):
        self.click_on(self.WRITE_US_LOCATOR)

    def fill_form_write_us(self):
        self.fill(self.NAME_LOCATOR, USER_AlESYA['name'])
        self.fill(self.EMAIL_WRITE_US_LOCATOR, USER_AlESYA['email'])
        self.fill(self.MASSAGE_INPUT_LOCATOR, 'Возможна ли доставка в Минск?')
        self.click_on(self.ACSSEPT_LOCATOR)
        self.click_on(self.SEND_LOCATOR)
        self.wait_for_visible(self.TEXT_LOCATOR)

    def assert_succsess_fill_form_write_us(self):
        self.assert_element_is_displayed(self.TEXT_LOCATOR)


