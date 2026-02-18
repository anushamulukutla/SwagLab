from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import get_config


class BasePage:
    """
    Base class for all page objects.

    Provides common Selenium WebDriver actions such as finding elements,
    clicking, entering text, checking visibility, and retrieving text or page title.
    Utilizes explicit waits for stability.
    """

    def __init__(self, driver):
        """
        Initialize the BasePage.

        Args:
            driver (webdriver.Chrome): The WebDriver instance to interact with the browser.
        """
        self.driver = driver
        self.config = get_config()
        self.wait = WebDriverWait(driver, self.config["timeout"])

    def find(self, locator):
        """
        Wait until the element is visible and return it.

        Args:
            locator (tuple): Locator tuple, e.g., (By.ID, "element_id").

        Returns:
            WebElement: The visible WebElement found.
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all(self, locator):
        """
        Wait until all elements are present and return them.

        Args:
            locator (tuple): Locator tuple, e.g., (By.CLASS_NAME, "elements_class").

        Returns:
            list[WebElement]: List of WebElements found.
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """
        Click on an element once it becomes visible.

        Args:
            locator (tuple): Locator tuple for the element to click.
        """
        self.find(locator).click()

    def enter_text(self, locator, text):
        """
        Clear any existing text and enter new text into an input field.

        Args:
            locator (tuple): Locator tuple for the input element.
            text (str): Text to enter into the input field.
        """
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator):
        """
        Check if an element is displayed on the page.

        Args:
            locator (tuple): Locator tuple for the element.

        Returns:
            bool: True if the element is displayed, False otherwise.
        """
        try:
            return self.find(locator).is_displayed()
        except:
            return False

    def get_text(self, locator):
        """
        Get the text content of an element.

        Args:
            locator (tuple): Locator tuple for the element.

        Returns:
            str: Text of the element.
        """
        return self.find(locator).text

    def get_title(self):
        """
        Get the current page title.

        Returns:
            str: Title of the current page.
        """
        return self.driver.title

    def is_element_visible(self, locator):
        """Return True if element is visible, False otherwise."""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False
