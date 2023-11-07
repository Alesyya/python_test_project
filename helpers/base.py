from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.WAIT_UNTIL = 10
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def wait_for_visible(self, locator):
        try:
            return WebDriverWait(self.driver, self.WAIT_UNTIL).until(
                EC.visibility_of_element_located((By.XPATH, locator)))
        except WebDriverException:
            assert False, f"Element {locator} not clicable"

    def wait_for_invisibility_of_element_located(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH, locator)))

    def click_on(self, locator):
        element = self.wait_for_visible(locator)
        element.click()

    def hard_click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].click();", element)

    def fill(self, locator, text):
        element = self.driver.find_element(By.XPATH, locator)
        element.clear()
        element.send_keys(text)

    def assert_element_is_displayed(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        assert element.is_displayed()

    def switch_between_windows(self):
        all_tabs = self.driver.window_handles
        first_tab = self.driver.current_window_handle
        for tab in all_tabs:
            if tab != first_tab:
                self.driver.switch_to.window(tab)
                break

    def assert_element_is_present(self, locator):
        try:
            self.wait_for_visible(locator)
        except Exception:
            assert False, f"Element {locator} is not present on the page"

    def assert_text_in_element(self, locator, expected_result):
        element = self.driver.find_element(By.XPATH, locator)
        element_text = element.text
        print(element_text, expected_result)
        assert element_text == expected_result, "Text not the same"

    def assert_text_get_value(self, locator, expected_result):
        element = self.driver.find_element(By.XPATH, locator)
        text_value = element.get_attribute("value")
        assert text_value == expected_result, "Text not the same"

    def assert_actual_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"
        return actual_url

    def assert_scroll(self):
        page_height = self.driver.execute_script("return document.documentElement.scrollHeight")
        self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        new_page_height = self.driver.execute_script("return document.documentElement.scrollHeight")
        assert new_page_height == page_height

    def assert_scroll_to_element(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)








