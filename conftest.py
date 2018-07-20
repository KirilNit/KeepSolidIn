import pytest
import selenium
from selenium import webdriver

@pytest.yield_fixture(scope="session")
def driver():
    _driver = webdriver.Chrome('C:\Users\Кирилл\AppData\Local\Programs\Python\Python37-32\Scripts')
    return _driver

@pytest.fixture(scope="session", autouse=True)
def stop(request, driver):
    def fin():
        driver.quit()
    request.addfinalizer(fin)

