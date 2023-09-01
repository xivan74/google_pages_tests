import pytest
from selene import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser_manage():
    print("Starting browser")
    yield browser
    browser.quit()
