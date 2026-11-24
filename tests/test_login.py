import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"

# ---------------------------------------------------------
# TEST CASE 1: Standard User (Happy Path)
# ---------------------------------------------------------
def test_standard_user_login(browser):
    print("\n--- Starting Test: Standard User Login ---")
    
    # Step 1: Open the browser and navigate to Swag Labs
    print("Step 1: Navigating to the website")
    browser.get(URL)

    # Step 2: Wait for the Username field to be visible
    print("Step 2: Waiting for username field")
    wait = WebDriverWait(browser, 10)
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    
    # Step 3: Enter the username "standard_user"
    print("Step 3: Entering username")
    username_field.send_keys("standard_user")

    # Step 4: Enter the password "secret_sauce"
    print("Step 4: Entering password")
    password_field = browser.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")

    # Step 5: Click the Login button
    print("Step 5: Clicking login button")
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()

    # Step 6: Verify we are on the Products page
    print("Step 6: Verifying successful login")
    wait.until(EC.url_contains("inventory.html"))
    assert "inventory.html" in browser.current_url
    
    # Verify the page title says "Products"
    page_title = browser.find_element(By.CLASS_NAME, "title").text
    assert page_title == "Products"
    
    print("--- Test Passed: Standard user logged in successfully ---")  