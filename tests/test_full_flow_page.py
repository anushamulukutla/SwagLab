import pytest
import re
from Pages import inventorypage
import json
from pathlib import Path
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFullFlowPage:

    @pytest.mark.tc_id("TC_CHK_009")
    def test_complete_single_order_successfully(self,driver,login_as_user):
        # Initialize page object
        inventory_page = inventorypage.Inventorypage(driver)
        # Step 1: login with standard user
        # Step 2: Wait until inventory page loads
        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item_name")))
        time.sleep(1)

        # Add products
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(1)  # SEE "Remove" button appear

        # Go to cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1) # SEE cart items

        # Checkout step 1 - Your Information
        driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "[data-test='firstName']").send_keys("Priya")
        driver.find_element(By.CSS_SELECTOR, "[data-test='lastName']").send_keys("Darshani")
        driver.find_element(By.CSS_SELECTOR, "[data-test='postalCode']").send_keys("12345")
        driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()
        time.sleep(1)  # SEE overview page

        # Checkout step 2 - Finish
        driver.find_element(By.CSS_SELECTOR, "[data-test='finish']").click()
        time.sleep(1)  # SEE thank you page

        # Assert thank you page
        thank_you_header = driver.find_element(By.CSS_SELECTOR,
                                               "[data-test='complete-header']").text.strip()
        assert thank_you_header == "Thank you for your order!"

        print("Complete checkout flow successfully done")

        # Back to cart page
        back_home_btn = driver.find_element(By.CSS_SELECTOR, "[data-test='back-to-products']")
        back_home_btn.click()
        time.sleep(1)


    @pytest.mark.tc_id("TC_CHK_010")
    def test_checkout_multiple_products_total(self, driver, login_as_user):
        # Initialize page object
        inventory_page = inventorypage.Inventorypage(driver)
        # Step 1: login with standard user
        # Step 2: Wait until inventory page loads
        WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item_name")))
        time.sleep(1)

        # Add multiple products
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-bike-light']").click()
        time.sleep(1)

        # Go to cart & VALIDATE
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)

        # .strip() removes invisible whitespace/newlines from web elements for clean matching
        cart_names = [e.text.strip() for e in
                      driver.find_elements(By.CLASS_NAME, "inventory_item_name")]
        expected_names = ["Sauce Labs Backpack", "Sauce Labs Bike Light"]
        assert cart_names == expected_names, f"Expected {expected_names}, got {cart_names}"

        # Calculate expected subtotal
        price_eles = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        item_prices = [float(e.text.replace("$", "")) for e in price_eles]
        expected_subtotal = sum(item_prices)
        print(f"Cart subtotal: ${expected_subtotal:.2f}")

        # Checkout...
        driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "[data-test='firstName']").send_keys("Priya")
        driver.find_element(By.CSS_SELECTOR, "[data-test='lastName']").send_keys("QA")
        driver.find_element(By.CSS_SELECTOR, "[data-test='postalCode']").send_keys("12345")
        driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()
        time.sleep(1)

        # Read checkout overview values BEFORE Finish (page will disappear)
        # Validates: cart subtotal + tax = total (core e-commerce business logic)
        subtotal_text = driver.find_element(By.CSS_SELECTOR, "[data-test='subtotal-label']").text
        tax_text = driver.find_element(By.CSS_SELECTOR, "[data-test='tax-label']").text
        total_text = driver.find_element(By.CSS_SELECTOR, "[data-test='total-label']").text

        # Parse $ amounts from text using regex (re module) - extracts just numbers
        subtotal = float(re.search(r"\$([0-9.]+)", subtotal_text).group(1))
        tax = float(re.search(r"\$([0-9.]+)", tax_text).group(1))
        total = float(re.search(r"\$([0-9.]+)", total_text).group(1))

        print(f"Overview: Subtotal=${subtotal}, Tax=${tax}, Total=${total}")

        # Cart subtotal matches overview subtotal (Relative tolerance of 0.1%)
        assert pytest.approx(subtotal, rel=1e-3) == expected_subtotal, "Subtotal mismatch!"
        # Overview math is correct: subtotal + tax = total (±0.1%)
        assert pytest.approx(total, rel=1e-3) == subtotal + tax, "Total calculation wrong!"

        # Scroll page a bit to see FINISH button
        finish_btn = driver.find_element(By.CSS_SELECTOR, "[data-test='finish']")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", finish_btn)
        time.sleep(1)
        finish_btn.click()

        # Assertion for thank you page
        assert "Thank you for your order!" in driver.find_element(
            By.CSS_SELECTOR, "[data-test='complete-header']").text
        time.sleep(1)
        print(" Multi-product checkout and totals VALIDATED!")

        # Back to cart page
        back_home_btn = driver.find_element(By.CSS_SELECTOR, "[data-test='back-to-products']")
        back_home_btn.click()
        time.sleep(1)

