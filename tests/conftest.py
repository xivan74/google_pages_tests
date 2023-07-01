import pytest
from selene import browser


@pytest.fixture(scope="function")
def browser_manage():
    print("Starting browser")
    yield browser
    browser.quit()
