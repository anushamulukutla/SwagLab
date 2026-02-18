Automation Framework – SauceDemo
Overview

This is a Selenium-based automation framework using pytest and the Page Object Model (POM) design pattern for the SauceDemo
 application.
The framework is implemented in Python and supports cross-browser testing, data-driven testing, and comprehensive reporting using Allure and HTML reports.

Project Structure
saucedemo ~/PycharmProjects/saucedemo
├── .venv
├── config
│   ├── config.py
│   └── config.yaml
├── Pages
│   ├── __init__.py
│   ├── base.py
│   └── Loginpage.py
├── Reports
├── testdata
│   ├── checkout.json
│   ├── login_data.json
│   └── product.json
├── tests
│   ├── __init__.py
│   └── test_home_page.py
├── utils
│   └── __init__.py
├── .gitignore
├── conftest.py
├── pytest.ini
├── README.md
├── requirements.txt


config/ – Contains configuration files (Python and YAML) for environment settings, URLs, credentials, etc.

Pages/ – Implements Page Object Model classes for application pages.

Reports/ – Stores HTML and Allure test execution reports.

testdata/ – Contains JSON files for test data used in data-driven tests.

tests/ – Contains pytest test scripts.

utils/ – Utility/helper functions used across the framework.

conftest.py – pytest fixtures for setup, teardown, and browser initialization.

pytest.ini – Configuration for pytest execution.

requirements.txt – Python dependencies.

Prerequisites

Python 3.10+

Selenium

pytest

pytest-html

Allure command-line (for generating Allure reports)

Browser drivers (e.g., ChromeDriver, GeckoDriver)

Virtual environment (.venv recommended)

Install dependencies:

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate     # Windows

# Install required packages
pip install -r requirements.txt

Configuration

config/config.yaml – Store environment variables, base URL, browser type, etc.

config/config.py – Reads YAML configuration and provides global access across tests.

Example snippet from config.yaml:

base_url: "https://www.saucedemo.com/"
browser: "chrome"
implicit_wait: 10

Test Execution
Run All Tests
pytest tests/ --alluredir=Reports/allure_raw --html=Reports/report.html --self-contained-html

Run Specific Test File
pytest tests/test_home_page.py --alluredir=Reports/allure_raw --html=Reports/report.html --self-contained-html

Generate Allure Report
allure serve Reports/allure_raw

Reporting

HTML Reports – Generated using pytest-html. Reports include test status, error screenshots, and detailed execution logs.

Allure Reports – Provides interactive dashboards, attachments, steps, and graphs for deeper test insights.

Test Data

JSON files under testdata/ folder are used for data-driven testing.

Example files:

login_data.json – Login credentials

checkout.json – Checkout details

product.json – Product data

Framework Features

Page Object Model (POM) for maintainable and scalable code

Data-driven testing using JSON files

Cross-browser testing support (Chrome, Firefox)

pytest fixtures for setup and teardown

HTML & Allure reporting for easy analysis

Config-driven design for easy environment management

Contribution Guidelines

Follow PEP8 coding standards

Create separate branches for new features or bug fixes

Use meaningful commit messages

Add tests for any new functionality

Update README and documentation for changes

