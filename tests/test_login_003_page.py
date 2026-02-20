import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Loginpage import LoginPage


class TestProblemUser:

    @pytest.mark.smoke
    def test_open_saucedemopage(self, login_page):
        # Verify home page loads successfully
        login_page.open()
        assert login_page.is_page_loaded()  # assert.is_page_loaded()

    @pytest.mark.tc_id("TC_LGN_003")

    def test_problem_user_login_TC_LGN_003(self, login_page, driver):
    # TC_LGN_003: Verify problem_user logs in but shows broken product images/UI issues

        # Login with problem_user (same as colleague did standard_user)
        login_page.enter_username("problem_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_btn()

        time.sleep(3)

    # Verify login success (different from locked_out)
        assert "inventory.html" in driver.current_url

    # Check broken images (your unique part)
        images = driver.find_elements(By.TAG_NAME, "img")
        broken_count = 0
        for img in images:
            if img.size['height'] == 0:
                broken_count += 1
        assert broken_count >= 6, f"Expected 6+ broken images"
