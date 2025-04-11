from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.home_page import HomePage
from Pages.login_page import LoginPage
import time

#Test case to login with valid credentials.
def test_valid_login(setup):
    try:
        #Step 1 : Click the login button from the homepage
        home = HomePage(setup)
        home.click_login()

        #Step 2: Enter valid email and password
        login = LoginPage(setup)
        email_input = WebDriverWait(setup,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@type='email']")))
        email_input.send_keys("sureshkannan.gss@gmail.com")
        time.sleep(2)
        password_input = WebDriverWait(setup,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@type='password']")))
        password_input.send_keys("Keerthana$dhiya16")
        time.sleep(2)
        login_button = WebDriverWait(setup,10).until(EC.element_to_be_clickable((By.XPATH,"(//a[text()='Login'])[1]")))
        login_button.click()


    # To check if the current url contains "Dashboard"
        wait = WebDriverWait(setup,15)
         #This will keep checking until the condition is true or time runs out
        wait.until(lambda driver: "dashboard" in driver.current_url.lower())
        print("login success! Current URL:", setup.current_url)
        assert "dashboard" in setup.current_url.lower()

    except Exception as e:
        print("test_valid_login failed:",e)

#Test case to log out from the account
def test_logout(setup):
    try:
        #Step 1: Click sign-out button from the login page
        home = HomePage(setup)
        home.click_login()
        login = LoginPage(setup)
        login.click_signout()
        WebDriverWait(setup,10).until(lambda driver: "dashboard" in driver.current_url.lower())

        #Step 2 : Wait for homepage to load after logout
        WebDriverWait(setup,10).until(EC.element_to_be_clickable((By.ID, "dropdown_title"))).click()
        WebDriverWait(setup,10).until(EC.element_to_be_clickable(((By.XPATH,"//div[text()='Sign Out']")))).click()
        print("Current URL after logout:", setup.current_url)
        assert "login" in setup.current_url.lower() or "guvi.in" in setup.current_url.lower()
    except Exception as e:
        print("Logout failed:", e)

#Test case to login with invalid credentials
def test_invalid_login(setup):
    try:
        #Click the login button from the homepage
        HomePage(setup).click_login()

        #Enter the invalid credentails
        login = LoginPage(setup)
        email_input = WebDriverWait(setup, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@type='email']")))
        email_input.send_keys("keerthanasuresh@gmail.com")
        password_input = WebDriverWait(setup, 10).until(EC.visibility_of_element_located((By.XPATH,"//input[@type='password']")))
        password_input.send_keys("keerthi$08")
        login_button = WebDriverWait(setup, 10).until(EC.element_to_be_clickable((By.XPATH, '(//a[text()="Login"])[1]')))
        login_button.click()



    #Wait for error message
        WebDriverWait(setup,10).until(EC.visibility_of_element_located((By.XPATH,"(//div[text()='Incorrect Email or Password'])[1]")))
        error = login.get_error_message()
        print("Error message shown:",error)
        assert "incorrect" in error
    except NoSuchElementException :
        print("Error message element not found")
    except AssertionError:
        print("Invalid login didn't shown the expected error message")













