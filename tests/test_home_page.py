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


