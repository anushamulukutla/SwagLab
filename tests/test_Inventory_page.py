import json
from pathlib import Path
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Load the testdata form testdata
TESTDATA_FILE = Path(__file__).parent.parent / "testdata" / "login_data.json"
#Open the test data file and load the data into a variable
with open (TESTDATA_FILE) as loginuser_data:
    login_test_data = json.load(loginuser_data)

class TestInventoryPage:

    @pytest.mark.smoke
    def test_open_saucedemopage(self, login_page):

        # Verify home page loads successfully
        login_page.open()
        assert login_page.is_page_loaded()
       # assert.is_page_loaded()
    @pytest.mark.tc_id("TC_INV_001")

    def test_standard_user_and_all_products(self,login_page, driver):

        #  # Step 1: Login as standard_user
        login_page.enter_username( login_test_data["standardUser"]["username"])
        login_page.enter_password(login_test_data["standardUser"]["password"])
        login_page.click_login_btn()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains("/inventory.html"))
        assert "/inventory.html" in driver.current_url

        # Step 2: Wait until products are visible
        product_titles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item_name")))
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, 300);") # Scroll to see all products
        time.sleep(1)
        # Extract product names
        actual_products = [title.text.strip() for title in product_titles]

        # Expected product list
        expected_products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)"
        ]

        # Verify count
        print(f"Total products displayed: {len(actual_products)}")

        # Verify names
        for product in expected_products:
            assert product in actual_products, f"{product} not found"