from selenium.webdriver.common.by import By

from config.config import get_config
from conftest import driver

from selenium.webdriver.common.by import By

class Inventorypage:
    def __init__(self, driver):
        self.driver = driver
        self.Inventory_price = (By.CSS_SELECTOR, ".inventory_item_price")

    def get_inventory_price_list(self,driver):
        inventory_price_ele = self.driver.find_elements(*self.Inventory_price)
        price_list = [price.text for price in inventory_price_ele]
        return price_list
    def get_all_products(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    