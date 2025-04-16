#  Mini Project 01: GUVI Web Application Automation

##  Project Title
**Automating GUVI Web Application Using Python Selenium and Pytest Framework**
##  Objective
This project aims to automate the test cases of the [GUVI web application](https://www.guvi.in) using the Python Selenium framework with Pytest. The automation includes both **positive** and **negative** test scenarios such as UI element validation, navigation checks, and login functionality testing.
##  Tools & Technologies Used
- Language: Python
- Automation Framework: Selenium WebDriver
- Test Runner: Pytest
- Browsers Supported: Chrome
Test Case No	Description
Test-Case-1	Validate whether the URL https://www.guvi.in is reachable and valid.
Test-Case-2	Validate the title of the webpage is: **“GUVI
Test-Case-3	Validate if the Login button is visible and clickable.
Test-Case-4	Validate if the Sign-up button is visible and clickable.
Test-Case-5	Click on the Sign-up button and verify if the sign-up page https://www.guvi.in/sign-in/ loads correctly.
Test-Case-6	Login with valid credentials and verify login success. Then logout and verify redirection.
Test-Case-7	Login using invalid credentials and capture the error message displayed.

##Notes

This project demonstrates Page Object Model (POM) for better code structure.

##POM Structure
Project_1/
│
├── Pages/                          # Page Object files
│   ├── __init__.py
│   ├── base_page.py                # Common Selenium methods
│   ├── home_page.py
│   └── login_page.py
│
├── Tests/                          # All test cases
│   ├── __init__.py
│   ├── test_homepage.py
│   ├── test_login.py             # (Consider separating logout test)
│
├── reports/                        # Generated HTML reports
│   ├── report1.html
│   ├── report2.html
│
├── conftest.py                     # Fixtures (driver setup, hooks)
