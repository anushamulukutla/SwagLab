import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestLoginPage:


    @pytest.mark.smoke
    def test_open_saucedemopage(self, login_page):
        """
          TC_HP_001: Verify home page loads successfully
          """
        login_page.open()
        assert login_page.is_page_loaded()
       # assert.is_page_loaded()

    class TestLogin:

        @pytest.mark.smoke
        def test_TC_LGN_001_valid_login_standard_user(self, login_page, driver):

            login_page.open()
            assert login_page.is_page_loaded(), "Login page did not load"

            login_page.login("standard_user", "secret_sauce")
            time.sleep(3)

            wait = WebDriverWait(driver, 10)

            wait.until(EC.url_contains("/inventory.html"))
            assert "/inventory.html" in driver.current_url, "Not redirected to /inventory.html"

            products_title = (By.CLASS_NAME, "title")  # SauceDemo shows "Products"
            title_el = wait.until(EC.visibility_of_element_located(products_title))
            assert title_el.text.strip() == "Products", "Products page not displayed"
