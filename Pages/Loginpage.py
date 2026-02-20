from selenium.webdriver.common.by import By
from Pages.base import BasePage
from config.config import get_config


class LoginPage(BasePage):
    """

    """
    #Locators:
    usename=(By.ID,"user-name")
    password=(By.ID,"password")
    login_btn=(By.NAME,"login-button")
    error_msg=(By.XPATH,"//div/h3[@data-test ='error']")

    def __init__(self, driver):
        super().__init__(driver)
        self.config = get_config()  # Load YAML config
        env = self.config.get("env", "qa")  # Default to 'qa' if missing
        self.url = self.config[env]["base_url"]  # Set the URL

    def open(self):
        """Navigate to the home page URL"""
        self.driver.get(self.url)

    def is_page_loaded(self):
        # returns True if login button is visible
        try:
            return self.driver.find_element(*self.login_btn).is_displayed()
        except:
            return False

    def enter_username(self,username):
        """Enter the username into the username field"""
        self.enter_text(self.usename, username)
    def enter_password(self,password):
        """Enter the password into the password field"""
        self.enter_text(self.password, password)
    def click_login_btn(self):
        """Click the login button to submit the form"""
        self.click(self.login_btn)
    def get_error_message(self):
        """Retrieve the error message text if login fails"""
        error_msg=self.get_text(self.error_msg)
        return error_msg

    # /

    from Pages.base import BasePage


    class LoginPage(BasePage):

        # Locators
        username = (By.ID, "user-name")
        password = (By.ID, "password")
        login_btn = (By.ID, "login-button")
        error_msg = (By.CSS_SELECTOR, "[data-test='error']")
        product_images = (By.CSS_SELECTOR, ".inventory_item_img img")

        def __init__(self, driver):
            super().__init__(driver)
            self.config = get_config()
            env = self.config.get("env", "qa")
            self.url = self.config[env]["url"]

        def open(self):
            self.driver.get(self.url)

        def enter_username(self, username):
            self.find_element(*self.username).send_keys(username)

        def enter_password(self, password):
            self.find_element(*self.password).send_keys(password)

        def click_login_btn(self):
            self.find_element(*self.login_btn).click()

        def get_error_message(self):
            return self.find_element(*self.error_msg).text

        def get_product_images(self):
            return self.driver.find_elements(*self.product_images)
    # /




