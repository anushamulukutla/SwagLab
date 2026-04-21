import pytest
from selenium import webdriver
from Pages.Loginpage import LoginPage
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tests.test_login_page import login_test_data


@pytest.fixture(scope="session")
def driver():

    # Create Chrome options properly
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # Disable password manager popups
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    # ✅ Use WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    # Initialize HomePage object
    page = LoginPage(driver)
    page.open()  # Navigate to home page URL
    return page
@pytest.fixture

def login_as_user(login_page):
    login_page.enter_username(login_test_data["standardUser"]["username"])
    login_page.enter_password(login_test_data["standardUser"]["password"])
    login_page.click_login_btn()
