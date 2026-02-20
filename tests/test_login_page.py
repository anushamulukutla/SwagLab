import json
import time
from pathlib import Path

import pytest
import testdata
from Pages.Loginpage import LoginPage

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
    @pytest.mark.tc_id("TC_LGN_001")

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

