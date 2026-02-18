import pytest

class TestLoginPage:


    @pytest.mark.smoke
    def test_open_saucedemopage(self, login_page):
        """
          TC_HP_001: Verify home page loads successfully
          """
        login_page.open()
        assert login_page.is_page_loaded()
       # assert.is_page_loaded()