import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkout_flow(browser):
    browser.get("https://www.saucedemo.com/")
    wait = WebDriverWait(browser, 10)

    # 1. Login first
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # 2. Add Backpack to cart 
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

    # 3. Go to Cart (clicking the cart icon link)
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 4. Click Checkout 
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # 5. Fill Checkout Info 
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("John")
    browser.find_element(By.ID, "last-name").send_keys("Doe")
    browser.find_element(By.ID, "postal-code").send_keys("12345")
    
    # 6. Click Continue 
    browser.find_element(By.ID, "continue").click()

    # 7. Click Finish 
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    # 8. Verify Success Message 
    complete_header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    assert complete_header.text == "Thank you for your order!"