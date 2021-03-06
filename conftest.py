import pytest
from selenium import webdriver


@pytest.yield_fixture(scope="session")
def driver():
    _driver = webdriver.Chrome()
    return _driver


@pytest.fixture(scope="session", autouse=True)
def stop(request, driver):
    def fin():
        driver.quit()
    request.addfinalizer(fin)