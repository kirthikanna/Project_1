from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver):
        #This initializes the class with a selenium webdriver instance
        self.driver = driver

    def get_title(self):
        #Returns the title of the current webpage
        return self.driver.title

    def is_element_visible(self,locator):
        #wait until the element is visible and return True
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False


    def is_element_clickable(self,locator):
        #wait until the element is clickable and return True
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locator))
            return True
        except:
            return False
    def click_element(self,locator):
        #Wait and click the element
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self,locator,text):
         #wait and send keys to input field
            element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located())
            element.send_keys(text)
