import pytest
from selenium import webdriver
from Pages.Loginpage import LoginPage


@pytest.fixture(scope="session")
def driver():
    # Setup: initialize WebDriver
    driver = webdriver.Chrome()  # or Firefox, Edge
    #driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver
    # Teardown: quit driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    # Initialize HomePage object
    page = LoginPage(driver)
    page.open()  # Navigate to home page URL
    return page
