import allure

from elements import HeaderElement
from pages import BuildingBoardProductPage
from pages import AllPromotionsPage


@allure.feature("Product price")
@allure.story("Check sale on product")
@allure.severity('minor')
def test_check_sale_on_product(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.click_on_all_promotions_locator()

    all_promotion_page = AllPromotionsPage(driver)
    all_promotion_page.click_on_product_locator()

    building_board_product_page = BuildingBoardProductPage(driver)
    building_board_product_page.check_sale()


@allure.feature("Favorites")
@allure.story("Add product to favorites")
@allure.severity('normal')
def test_add_product_to_favorites(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.click_on_all_promotions_locator()

    all_promotion_page = AllPromotionsPage(driver)
    all_promotion_page.click_on_product_locator()

    building_board_product_page = BuildingBoardProductPage(driver)
    building_board_product_page.click_on_favorites_locator()
    building_board_product_page.checking_product_is_in_favorites()