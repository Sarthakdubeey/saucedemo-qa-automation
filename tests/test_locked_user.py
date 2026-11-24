import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_locked_out_user(browser):
    browser.get("https://www.saucedemo.com/")
    wait = WebDriverWait(browser, 10)

    # Input locked_out_user credentials (shown in your first screenshot)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("locked_out_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # Click login
    browser.find_element(By.ID, "login-button").click()

    # Wait for and verify the error message container
    error_container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))
    
    # Assert the exact text
    expected_error = "Epic sadface: Sorry, this user has been locked out."
    assert error_container.text == expected_error