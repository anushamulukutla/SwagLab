import pytest
import re
from Pages import inventorypage
import json
from pathlib import Path
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestInventoryPage:

    @pytest.mark.tc_id("TC_INV_003")
    def test_inventory_Product_price_displayed(self,driver,login_as_user):
        """
        TC_INV_003: Verify product prices are displayed correctly on the inventory page
        """
        Inventorypage=inventorypage.Inventorypage(driver)
        # Step 1: login with standard user
        # Step 2: Get all price elements on the inventory page
        List_prices = Inventorypage.get_inventory_price_list(self)
        print("List of product prices:", List_prices)
        #asser the fomat of the prices
        pattern_price = re.compile(r'^\$\d+\.\d{2}$')
        for price_text in List_prices:
            assert re.match(pattern_price, price_text), f"Price format incorrect: {price_text}"
            print("asserted price format for price:", price_text)

    @pytest.mark.tc_id("TC_INV_001")
    def test_standard_user_and_all_products(self, driver, login_as_user):
        # Initialize page object
        inventory_page = inventorypage.Inventorypage(driver)
        # Step 1: login with standard user
        # Step 2: Wait until inventory page loads
        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
        WebDriverWait(driver, 10).until( EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item_name")))
        time.sleep(1)
        # Step 3: Scroll a bit to ensure all products are visible
        driver.execute_script("window.scrollBy(0, 300);")  # Scroll to see all products
        time.sleep(1)

        # Step 4:Get all product names from the page object
        actual_products = [p.text.strip() for p in inventory_page.get_all_products()]

        # Step 5: Expected products
        expected_products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie",
            "Test.allTheThings() T-Shirt (Red)"
        ]

        # Step 6: Assert exact match
        assert actual_products == expected_products, "Product list does not match expected list"

        # Step 7: Print total products and names
        print(f"Total products displayed: {len(actual_products)}")
        for product in actual_products:
            print(product)


