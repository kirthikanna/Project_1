from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):
        return self.driver.title

    def is_element_visible(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except TimeoutException:
            print(f"[ERROR] Element not visible: {locator}")
            return False

    def is_element_clickable(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            print(f"[ERROR] Element not clickable: {locator}")
            return False

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
