from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.base_page import BasePage

class LoginPage(BasePage):
    EMAIL_FIELD = (By.XPATH,"//input[@type='email']")
    PASSWORD_FIELD = (By.XPATH,"//input[@type='password']")
    SUBMIT_BUTTON = (By.XPATH,"(//a[text()='Login'])[1]")
    DROP_DOWN = (By.ID,"dropdown_title")
    SIGN_OUT_BUTTON = (By.XPATH,"//div[text()='Sign Out']")
    ERROR_MESSAGE = (By.XPATH,"(//div[text()='Incorrect Email or Password'])[1]")

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.EMAIL_FIELD)).send_keys(email)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def click_signout(self):
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable(self.SIGN_OUT_BUTTON)).click()


    def get_error_message(self):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text
