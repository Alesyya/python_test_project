import allure

from pages import MainPage


@allure.feature("Title")
@allure.story("Check title of main page")
@allure.severity('minor')
def test_main_page_title(driver, accept_cookies):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_main_page_title()


@allure.feature("Page")
@allure.story("Scroll main page")
@allure.severity('blocker')
def test_scroll_page(driver, accept_cookies):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_scroll_page()


@allure.feature("Product")
@allure.story("Button with sale")
@allure.severity('normal')
def test_button_with_sale(driver, accept_cookies):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_on_product_with_sale_button()
    main_page.assert_visible_persent_of_sale_text()


@allure.feature("Product")
@allure.story("Button with Surprise")
@allure.severity('normal')
def test_button_with_surprise(driver, accept_cookies):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_on_product_with_surprise_button()
    main_page.assert_visible_present_text()


@allure.feature("Product")
@allure.story("Button with super price")
@allure.severity('normal')
def test_button_with_super_price(driver, accept_cookies):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_on_super_price_button()
    main_page.assert_visible_super_price_text()


@allure.feature("Product")
@allure.story("Button with discounted")
@allure.severity('normal')
def test_button_with_discounted_product(driver, accept_cookies):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_on_discounted_product_button()
    main_page.assert_visible_discounted_product_text()