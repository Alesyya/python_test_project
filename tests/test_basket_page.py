from elements import HeaderElement
from pages import MainPage
from pages import BasketPage


def test_add_product_to_basket(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_product_to_basket_button()

    header_element = HeaderElement(driver)
    header_element.open()
    header_element.click_on_basket()

    basket_page = BasketPage(driver)
    basket_page.assert_items_is_add_to_basket()


def test_delete_from_basket(driver, add_product_to_basket):
    basket_page = BasketPage(driver)
    basket_page.click_on_delete_from_basket_locator()
    basket_page.click_on_confirm_delete_locator()
    basket_page.assert_text_succsses_delete_product()


def test_add_to_favorites(driver, add_product_to_basket):
    basket_page = BasketPage(driver)
    basket_page.click_on_add_to_favorites()
    basket_page.assert_text_succsses_add_to_favorites()


def test_add_product_quantity(driver, add_product_to_basket):
    basket_page = BasketPage(driver)
    basket_page.click_on_plus_locator()
    basket_page.assert_text_add_count_product()


def test_add_additional_service(driver, add_product_to_basket):
    basket_page = BasketPage(driver)
    basket_page.click_on_additional_service_locator()
    basket_page.assert_count_additional_service()


def test_delete_additional_service(driver, add_product_to_basket, add_additional_service):
    basket_page = BasketPage(driver)
    basket_page.click_on_additional_service_locator()
    basket_page.assert_delete_additional_service()