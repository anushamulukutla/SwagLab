import csv
import json
import time
from pathlib import Path
import pytest

from Pages.checkoutpage import checkoutpage

# Load the testdata form testdata
TESTDATA_FILE = Path(__file__).parent.parent / "testdata" / "checkout.json"
#Open the test data file and load the data into a variable
with open (TESTDATA_FILE) as checkoutuser_data:
    check_outuser_data = json.load(checkoutuser_data)
class TestCheckoutPage:


    def test_checkout_process(self,login_as_user,driver):
        checkout_page = checkoutpage(driver)
       #login


        #add to cart
        checkout_page.click_add_to_cart_btn_sauce_labs_backpack()
        checkout_page.click_add_to_cart_btn_sauce_labs_bike_light()

        #CHECKOUT
        checkout_page.click_cart()
        checkout_page.click_checkout_btn()

        #ENTER FIRSTNAME
        checkout_page.enter_checkout_firstname(check_outuser_data["validCustomer"]["firstName"])
        #ENTER LASTNAME
        checkout_page.enter_checkout_lastname(check_outuser_data["validCustomer"]["lastName"])
        #ENTER POSTAL CODE
        checkout_page.enter_checkout_postalcode(check_outuser_data["validCustomer"]["postalCode"])
        #CLickOn Continue
        checkout_page.click_checkout_continue_btn()
        time.sleep(5)
        #get the list of items
        items = checkout_page.get_cart_items()

        csv_file = "cart_items.csv"

        with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["quantity", "name", "description", "price"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)  # ✅ pass file

            writer.writeheader()
            writer.writerows(items)

        print("Cart items saved to cart_items.csv")

        itemsprice=checkout_page.get_list_of_price()
        taxamount=checkout_page.get_tax_amount()
        Total_price=taxamount+itemsprice
        print("Total price:", Total_price)
        Actual_total_price = checkout_page.get_total_price(self)
        assert Total_price == Actual_total_price , "Total price does not match expected value"


       # for item in items:
          #  print(f"Quantity: {item['quantity']}, Name: {item['name']}, Description: {item['description']}, Price: {item['price']}")


