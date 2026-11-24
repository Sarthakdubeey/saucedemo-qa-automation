import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    print("\n[SETUP] Starting Chrome Browser...")
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # Uncomment to run without UI
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    yield driver
    
    print("\n[TEARDOWN] Closing Browser...")
    driver.quit()