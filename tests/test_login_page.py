import json
from pathlib import Path
import time
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


class TestLoginPage:


    @pytest.mark.smoke
    def test_open_saucedemopage(self, login_page):
        """
           Verify home page loads successfully
          """
        login_page.open()
        assert login_page.is_page_loaded()
       # assert.is_page_loaded()
    @pytest.mark.tc_id("TC_LGN_002")

    def test_login_with_lock_out_user(self,login_page):
        """
        TC_LGN_002: Verify login with locked out user fails
        :return:
        """
        login_page.enter_username(login_test_data["lockedOutUser"]["username"])
        login_page.enter_password(login_test_data["lockedOutUser"]["password"])
        login_page.click_login_btn()

        time.sleep(5)
        self.Actual_text=login_page.get_error_message()
        self.Expected_text="Epic sadface: Sorry, this user has been locked out."
        assert self.Actual_text == self.Expected_text,"Error message does not match expected for locked out user"

    @pytest.mark.tc_id("TC_LGN_001")
    def test_login_with_standard_user(self, login_page, driver):

        login_page.enter_username( login_test_data["standardUser"]["username"])
        login_page.enter_password(login_test_data["standardUser"]["password"])
        login_page.click_login_btn()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains("/inventory.html"))

        assert "/inventory.html" in driver.current_url

    @pytest.mark.smoke
    def test_open_saucedemopage(self, login_page):
        # Verify home page loads successfully
        login_page.open()
        assert login_page.is_page_loaded()  # assert.is_page_loaded()

    # @pytest.mark.tc_id("TC_LGN_003")
    #
    # def test_problem_user_login_TC_LGN_003(self, login_page, driver):
    # # TC_LGN_003: Verify problem_user logs in but shows broken product images/UI issues
    #
    #     # Login with problem_user (same as colleague did standard_user)
    #     login_page.enter_username("problem_user")
    #     login_page.enter_password("secret_sauce")
    #     login_page.click_login_btn()
    #
    #     # time.sleep(3)
    #
    #     wait = WebDriverWait(driver, 10)
    #     wait.until(EC.url_contains("inventory.html"))
    # # Verify login success (different from locked_out)
    #     assert "inventory.html" in driver.current_url
    #
    # # Check broken images (your unique part)
    #     images = driver.find_elements(By.TAG_NAME, "img")
    #     broken_count = 0
    #     for img in images:
    #         if img.size['height'] == 0:
    #             broken_count += 1
    #     assert broken_count >= 6, f"Expected 6+ broken images"

    @pytest.mark.tc_id("TC_LGN_003")
    def test_problem_user_login_TC_LGN_003(self, login_page, driver):
        login_page.enter_username("problem_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_btn()

        wait = WebDriverWait(driver, 10)
        wait.until(EC.url_contains("inventory.html"))
        assert "inventory.html" in driver.current_url

        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item_img img")))
        images = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_img img")

        srcs = [img.get_attribute("src") for img in images]
        unique_srcs = set(srcs)

        print("Total images:", len(srcs))
        print("Unique images:", len(unique_srcs))

        # If there's a mismatch/duplication bug, unique images will be less than total
        assert len(unique_srcs) < len(srcs), "Expected duplicate/mismatched product images for problem_user"