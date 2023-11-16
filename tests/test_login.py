import allure

from elements import HeaderElement
from pages import LoginPage
from data.users import (USER_AlESYA, USER_WITH_NONEXISTENT_ACCOUNT, USER_WITH_INVALID_EMAIL)


@allure.feature("Registration")
@allure.story("Check registration")
@allure.severity('critical')
def test_check_registration(driver):
    header_element = HeaderElement(driver)
    header_element.click_on_account_locator()

    login_page = LoginPage(driver)
    login_page.click_on_enter_button()
    login_page.click_on_registration_button_locator()
    login_page.enter_email_random()
    login_page.click_on_countinue_button_locator()
    login_page.click_on_obrabotka_locator()
    login_page.assert_access_registration()


@allure.feature("Login")
@allure.story("Enter in account success")
@allure.severity('critical')
def test_success_loggin(driver):
    header_element = HeaderElement(driver)
    header_element.click_on_account_locator()

    login_page = LoginPage(driver)
    login_page.click_on_enter_button()
    login_page.fill_email(USER_AlESYA['email'])
    login_page.fill_password(USER_AlESYA['password'])
    login_page.click_on_enter_in_account_locator_for_login()
    header_element.click_on_account_locator()
    login_page.assert_text_success_login()


@allure.feature("Login")
@allure.story("Check incorrect input email")
@allure.severity('critical')
def test_input_incorrect_email_for_login(driver):
    header_element = HeaderElement(driver)
    header_element.click_on_account_locator()

    login_page = LoginPage(driver)
    login_page.click_on_enter_button()
    login_page.fill_email(USER_WITH_INVALID_EMAIL['email'])
    login_page.fill_password(USER_WITH_INVALID_EMAIL['password'])
    login_page.click_on_enter_in_account_locator()
    login_page.assert_massage_invalid_email()


@allure.feature("Login")
@allure.story("Check enter user with nonexistene account")
@allure.severity('critical')
def test_enter_user_with_nonexistent_account(driver):
    header_element = HeaderElement(driver)
    header_element.click_on_account_locator()

    login_page = LoginPage(driver)
    login_page.click_on_enter_button()
    login_page.fill_email(USER_WITH_NONEXISTENT_ACCOUNT['email'])
    login_page.fill_password(USER_WITH_NONEXISTENT_ACCOUNT['password'])
    login_page.click_on_enter_in_account_locator()
    login_page.assert_massage_no_such_account()