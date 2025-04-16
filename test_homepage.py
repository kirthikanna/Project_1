# import time
import pytest
from Pages.home_page import HomePage

def test_url_validity(setup):
    """Test that URL contains 'guvi.in'"""
    print("Verifying URL contains 'guvi.in'")
    assert "guvi.in" in setup.current_url, "URL validation failed"
    print("URL contains 'guvi.in'")

def test_title(setup):
    """Test page title matches expected"""
    print("Verifying page title matches expected value")
    expected_title = "GUVI | Learn to code in your native language"
    assert setup.title == expected_title, "Title mismatch"
    print("Page title is correct")

def test_login_button_visibility(setup):
    """Test login button is visible"""
    page = HomePage(setup)
    print("Checking if login button is visible")
    assert page.is_element_visible(HomePage.LOGIN_BUTTON), "Login button not visible"
    print("Login button is visible")

def test_login_button_clickable(setup):
    """Test login button is clickable"""
    page = HomePage(setup)
    print("Checking if login button is clickable")
    assert page.is_element_clickable(HomePage.LOGIN_BUTTON), "Login button not clickable"
    print("Login button is clickable")


def test_signup_button_visibility(setup):
    """Test signup button is visible"""
    page = HomePage(setup)
    print("Checking if signup button is visible")
    assert page.is_element_visible(HomePage.SIGNUP_BUTTON), "Signup button not visible"
    print("Signup button is visible")

def test_signup_button_clickable(setup):
    """Test signup button is clickable"""
    page = HomePage(setup)
    print("Checking if signup button is clickable")
    assert page.is_element_clickable(HomePage.SIGNUP_BUTTON), "Signup button not clickable"
    print("Signup button is clickable")


def test_signup_navigation(setup):
    """Test signup button navigates to register page"""
    page = HomePage(setup)
    print("Clicking signup button and verifying navigation")
    page.click_signup()
    print(f"Current URL after click: {setup.current_url}")
    assert "register" in setup.current_url.lower(), "Navigation to register page failed"
    print("Successfully navigated to register page")
