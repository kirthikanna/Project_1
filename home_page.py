from selenium.webdriver.common.by import By
from Pages.base_page import BasePage

class HomePage(BasePage):
    LOGIN_BUTTON = (By.ID,"login-btn")
    SIGNUP_BUTTON = (By.XPATH,"//a[text()='Sign up']")

    def click_signup(self):
        self.click_element(self.SIGNUP_BUTTON)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)
