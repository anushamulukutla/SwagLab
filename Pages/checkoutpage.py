import self
from selenium.webdriver.common.by import By

from Pages.base import BasePage


class checkoutpage(BasePage):

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

        self.Add_to_cart_btn_Sauce_labs =(By.ID,"add-to-cart-sauce-labs-backpack")
        self.Add_to_cart_btn_Sauce_labs_bike_light =(By.ID,"add-to-cart-sauce-labs-bike-light")
        self.Add_to_cart=(By.CSS_SELECTOR,".shopping_cart_container")
        self.checkout_btn=(By.ID,"checkout")
        self.checkout_firstname=(By.ID,"first-name")
        self.checkout_lastname=(By.ID,"last-name")
        self.checkout_postalcode=(By.ID,"postal-code")
        self.checkout_continue_btn=(By.CSS_SELECTOR,"#continue")
        self.checkout_list_price=(By.CSS_SELECTOR,".cart_list")
        self.qunantity=(By.CLASS_NAME,"cart_quantity")
        self.item_name=(By.CLASS_NAME,"inventory_item_name")
        self.item_description=(By.CLASS_NAME,"inventory_item_desc")
        self.item_price=(By.CLASS_NAME,"inventory_item_price")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.total_price=(By.XPATH,"//dic[@data-test='total_label']")
        self.tax_amount=(By.XPATH,"//div[@data-test='tax-label']")



    def click_add_to_cart_btn_sauce_labs_backpack(self):
        self.driver.find_element(*self.Add_to_cart_btn_Sauce_labs).click()

    def click_add_to_cart_btn_sauce_labs_bike_light(self):
        self.driver.find_element(*self.Add_to_cart_btn_Sauce_labs_bike_light).click()
    def click_cart(self):
        self.driver.find_element(*self.Add_to_cart).click()
    def click_checkout_btn(self):
        self.click(self.checkout_btn)
    def enter_checkout_firstname(self,firstname):
        self.enter_text(self.checkout_firstname,firstname)
    def enter_checkout_lastname(self,lastname):
        self.enter_text(self.checkout_lastname,lastname)
    def enter_checkout_postalcode(self,postalcode):
        self.enter_text(self.checkout_postalcode,postalcode)
    def click_checkout_continue_btn(self):
        self.click(self.checkout_continue_btn)
    def get_list_of_items(self):
        lsit_items =self.find_all(self.checkout_list_price)
        return lsit_items

    def get_cart_items(self):
        cart_items = self.find_all(self.cart_items)
        cart_list = []

        for item in cart_items:
            quantity = item.find_element(*self.qunantity).text
            name = item.find_element(*self.item_name).text
            description = item.find_element(*self.item_description).text
            price = item.find_element(*self.item_price).text

            cart_list.append({
                "quantity": quantity,
                "name": name,
                "description": description,
                "price": price
            })

        return cart_list

    def get_list_of_price(self):
        import csv

        prices = []

        with open("cart_items.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                price = row["price"]  # "$29.99"
                prices.append(price)
        total = sum(float(price.replace("$", "")) for price in prices)
        print("Total price:", total)
        return total

    def get_total_price(self,driver):
        total_price_element = driver.find_element(*self.total_price)
        total_price_text = total_price_element.text  # "Total: $49.98"
        total_price = float(total_price_text.replace("Total: $", ""))
        return total_price

    def get_tax_amount(self):  # ✅ CORRECT
        tax_amount_element = self.driver.find_element(*self.tax_amount)
        return tax_amount_element.text



        #print("Prices:", sum(int(prices)))



