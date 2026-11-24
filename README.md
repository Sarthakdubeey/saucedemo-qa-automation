
# SauceDemo QA Automation Project

## Project Overview
Automated testing of the SauceDemo e-commerce website using Python, Selenium WebDriver and Pytest.

## Website
https://www.saucedemo.com/

## Technologies Used
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Visual Studio Code
- Google Chrome

## Test Scenarios

1. Standard User Login
2. Locked Out User Login
3. Complete Checkout Flow

## Project Structure

saucedemo-tests/
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_checkout.py
│   └── test_locked_user.py
├── reports/
│   └── test_report.html
├── .gitignore
├── README.md
├── test_plan.md
├── bug_reports.md
└── requirements.txt

## Execution

Install dependencies:

pip install -r requirements.txt

Run tests:

python -m pytest tests -v -s

Generate HTML report:

python -m pytest tests -v --html=reports/test_report.html --self-contained-html

## Test Results

Total Tests: 3
Passed: 3
Failed: 0

## Author
Sarthak Dubey
