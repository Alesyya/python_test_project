from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from data.users import USER_AlESYA
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOption
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.firefox.options import Options as FirefoxOption
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption('--headless',
                     default='False',
                     help='headless options: "yes" or "no"')
    parser.addoption('--browser',
                     default='chrome',
                     help='option to define type of browser')


def create_chrome(headless=True):
    chrome_option = ChromeOption()
    if headless == 'True':
        chrome_option.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_option)
    return driver


def create_firefox(headless=True):
    ff_option = FirefoxOption()
    if headless:
        ff_option.add_argument('--headless')
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=ff_option)
    return driver


@pytest.fixture(scope='function', autouse=True)
def driver(request):
    browser = request.config.getoption('--browser')
    headless = request.config.getoption('--headless')

    if browser == 'chrome':
        driver = create_chrome(headless)
    elif browser == 'ff':
        driver = create_firefox(headless)
    else:
        raise ValueError(f"Invalid browser option: {browser}")

    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def accept_cookies(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.accept_cookies()


@pytest.fixture(autouse=False)
def login(request):
    login = LoginPage(request.node.funcargs['driver'])
    login.login(USER_AlESYA)


@pytest.fixture(autouse=False)
def add_product_to_basket(driver):
    basket_page = BasketPage(driver)
    basket_page.add_to_basket()


@pytest.fixture(autouse=False)
def add_additional_service(driver):
    basket_page = BasketPage(driver)
    basket_page.add_additional_service()







