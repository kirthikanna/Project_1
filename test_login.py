from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from Pages.home_page import HomePage
from Pages.login_page import LoginPage
import time

#Test case to login with valid credentials.
def test_valid_login(setup):
    home = HomePage(setup)
    home.click_login()
    print("Navigated to login page")

    login = LoginPage(setup)
    login.enter_email("sureshkannan.gss@gmail.com")
    time.sleep(1)
    login.enter_password("Keerthana$dhiya16")
    time.sleep(1)
    login.click_login_button()

    # Wait for sign out element to confirm login
    WebDriverWait(setup, 15).until(
        EC.presence_of_element_located((By.XPATH,"//div[text()='Sign Out']"))
    )
    print("Login successful! Sign out button is visible.")

    assert "sign-in" not in setup.current_url.lower()


#Test case to log out from the account
def test_logout(setup):
    home = HomePage(setup)
    home.click_login()
    print("Navigated to login page for logout")

    login = LoginPage(setup)
    login.enter_email("sureshkannan.gss@gmail.com")
    login.enter_password("Keerthana$dhiya16")
    login.click_login_button()

    # Click the user dropdown/profile icon before Sign Out
    WebDriverWait(setup, 10).until(
        EC.element_to_be_clickable((By.ID, "dropdown_title"))
    ).click()

    # Wait for sign out button to confirm login
    WebDriverWait(setup, 15).until(
        EC.element_to_be_clickable((By.XPATH,"//div[text()='Sign Out']"))
    )

    login.click_signout()

    # Wait for login button to reappear to confirm logout
    WebDriverWait(setup, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//a[text()='Login'])[1]"))
    )
    print("Logout successful")


#Test case to login with invalid credentials
def test_invalid_login(setup):
    home = HomePage(setup)
    home.click_login()
    print("Navigated to login page for invalid credentials")

    login = LoginPage(setup)
    login.enter_email("keerthanasuresh@gmail.com")
    login.enter_password("keerthi$08")
    login.click_login_button()

    error = WebDriverWait(setup, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Incorrect Email or Password')]"))
    )
    print("Error message shown:", error.text)
    assert "Incorrect Email or Password" in error.text
















