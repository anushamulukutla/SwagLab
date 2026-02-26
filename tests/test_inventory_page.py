import pytest
import re
from Pages import inventorypage
from tests.test_login_page import login_test_data


class TestInventoryPage:

    @pytest.mark.tc_id("TC_INV_003")
    def test_inventory_Product_price_displayed(self,driver,login_as_user):
        """
        TC_INV_003: Verify product prices are displayed correctly on the inventory page
        :return:
        """
        Inventorypage=inventorypage.Inventorypage(driver)
        #step1: loginfwith standard user
        # Step 2: Get all price elements on the inventory page
        List_prices = Inventorypage.get_inventory_price_list(self)
        print("List of product prices:", List_prices)
        #asser the fomat of the prices
        pattern_price = re.compile(r'^\$\d+\.\d{2}$')
        for price_text in List_prices:
            assert re.match(pattern_price, price_text), f"Price format incorrect: {price_text}"
            print("asserted price format for price:", price_text)





