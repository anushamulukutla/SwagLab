# SauceDemo UI Automation Framework

## Overview

This project is a scalable and maintainable **UI Automation Framework** developed using **Python**, **Selenium WebDriver**, and **pytest**, following the **Page Object Model (POM)** design pattern. The framework is designed to automate functional testing of the SauceDemo web application.

It supports **data-driven testing**, **centralized configuration**, and **advanced reporting using Allure and HTML reports**, making it suitable for real-world enterprise automation projects.

---

## Tech Stack

- Language: Python
- Automation Tool: Selenium WebDriver
- Test Framework: pytest
- Design Pattern: Page Object Model (POM)
- Reporting: Allure Reports, pytest-html
- Test Data: JSON
- Configuration: YAML
- Version Control: Git

---

---

## Framework Features

- Page Object Model (POM) implementation
- Data-driven testing using JSON files
- Centralized configuration using YAML
- pytest fixtures for browser setup and teardown
- HTML reporting using pytest-html
- Allure reporting for advanced visualization
- Modular and scalable framework design
- Easy integration with CI/CD tools

---

## Prerequisites

Ensure the following are installed on your system:

- Python 3.10 or higher
- pip
- Google Chrome browser
- ChromeDriver (matching your browser version)
- Allure Command Line Tool (optional, for Allure reports)

---

## Installation Steps

### 1. Clone the Repository
``bash
git clone <your-repository-url>
cd saucedemo

### 2.Create Virtual Environment
python -m venv .venv

###3.Activate Virtual Environment
MAC: source .venv/bin/activate
Windows:.venv\Scripts\activate

### 4. Install Dependencies
pip install -r requirements.txt
----
### Configuration
config/config.yaml

EXAMPLE: 
base_url: https://www.saucedemo.com/
browser: chrome
implicit_wait: 10
---
## Run all tests
pytest tests/
----
## Run tests with HTML report
pytest tests/ --html=Reports/report.html --self-contained-html

---
## Run tests with Allure report
pytest tests/ --alluredir=Reports/allure-results
---
## View Allure Report
allure serve Reports/allure-results

## Run specific test file
pytest tests/test_home_page.py

##Test Data Management
Test data is stored in JSON files inside the testdata folder:
login_data.json
checkout.json
product.json
This enables data-driven testing and improves flexibility.

Page Object Model (POM)
Page Object Model (POM) is a design pattern in Selenium that creates an object repository for storing all web elements. It helps reduce code duplication and improves test case maintenance.

In POM, each web page of an application is considered as a class file. Each class file contains only the web page elements. Using these elements, you can perform operations on the website under test.

Why Page Object Model?
Helps with easy maintenance.
Reusability of code.
Readability and reliability of scripts.
Provides structure to the automation framework.



##Future Enhancements
CI/CD integration (GitHub Actions / Jenkins)
Cross-browser execution support
Parallel test execution
Docker integration
Screenshot capture on failure













