from pages import MainPage


def test_main_page_title(driver, accept_cookies):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_main_page_title()


def test_scroll_page(driver, accept_cookies):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_scroll()


def test_button_with_sale(driver, accept_cookies):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_on_product_with_sale_button()
    main_page.assert_visible_persent_of_sale_text()


def test_button_with_surprise(driver, accept_cookies):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_on_product_with_surprise_button()
    main_page.assert_visible_present_text()


def test_button_with_super_price(driver, accept_cookies):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_on_super_price_button()
    main_page.assert_visible_super_price_text()


def test_button_with_discounted_product(driver, accept_cookies):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_on_discounted_product_button()
    main_page.assert_visible_discounted_product_text()