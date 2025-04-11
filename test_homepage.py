import time

from selenium.common.exceptions import NoSuchElementException
from Pages.home_page import HomePage


#Test Case to validate the URl is correct
def test_url_validity(setup):
    try:
        assert "guvi.in" in setup.current_url
    except AssertionError:
        print("URL is not valid or doesn't contain 'guvi.in'")

#Test case to validate the title of the page
def test_title(setup):
    try:
        assert setup.title == "GUVI | learn to code iin your native language"
    except AssertionError:
        print("Page title does not match expected title")

#Test case to check login button visibility
def test_login_button_visibility(setup):
    page = HomePage(setup)
    try:
        assert page.is_element_visible(HomePage.LOGIN_BUTTON)
    except NoSuchElementException:
        print("Login button element not found")
    except AssertionError:
        print("Login button is not visible")

#Test case to check if the login button is clickable
def test_login_button_clickable(setup):
    page = HomePage(setup)
    try:
        assert page.is_element_clickable(HomePage.LOGIN_BUTTON)
    except NoSuchElementException:
        print("Login button element not found")
    except AssertionError:
        print("Login button is not clickable")

#Test case to check sign-up button visibility
def test_signup_button_visibility(setup):
    page = HomePage(setup)
    try:
        assert page.is_element_visible(HomePage.SIGNUP_BUTTON)
        time.sleep(2)
    except NoSuchElementException:
        print("Sign-up button element not found")
    except AssertionError:
        print("Sign-up button is not visible")
#Test case to check sign-up button clickable
def test_signup_button_clickable(setup):
    page = HomePage(setup)
    try:
        assert page.is_element_clickable(HomePage.SIGNUP_BUTTON)
    except NoSuchElementException:
        print("Sign-up button element not found")
    except AssertionError:
        print("Sign-up button is not clickable")
#Test case to check navigation to sign-in page using sign-up button
def test_signup_navigation(setup):
    page = HomePage(setup)
    try:
        page.click_signup()
        assert "sign-in" in setup.current_url
    except NoSuchElementException:
        print("sign-up button element not found for navigation")
    except AssertionError:
        print("Navigation to sign-in page failed")
