from elements import HeaderElement


def test_21vek_logo(driver):
    header = HeaderElement(driver)
    header.open()
    header.assert_visible_logo()


def test_visible_text_refrigerators(driver, accept_cookies):
    header = HeaderElement(driver)
    header.open()
    header.assert_correct_visible_text_product()


def test_choose_country(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.open()
    header_element.click_on_city_locator()
    header_element.click_on_but_close_locator()
    header_element.click_on_select_city_from_list()
    header_element.click_on_save_button_locator()
    header_element.assert_choose_country()


def test_choose_country_incorrect(driver, accept_cookies):
    header_element = HeaderElement(driver)
    header_element.open()
    header_element.click_on_city_locator()
    header_element.click_on_but_close_locator()
    header_element.fill_country_field()
    header_element.click_on_save_button_locator()
    header_element.assert_incorrect_input_country()