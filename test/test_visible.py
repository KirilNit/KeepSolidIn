from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def test_visiblee(driver):
    driver.get('https://www.vpnunlimitedapp.com/en')
    plBut = driver.find_element_by_xpath("//div[@class='pulse2']/ancestor::a")

    wait = WebDriverWait(driver, 9)
    plBut.click()
    wait.until(ec.visibility_of(driver.find_element_by_xpath("//video")))
