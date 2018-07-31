from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

def test_disappear(driver):
    driver.get('https://www.vpnunlimitedapp.com/en/pricing')
    wait = WebDriverWait(driver, 10)
    el1 = driver.find_element_by_xpath("//a[@class='prices_cnt--item']")
    el1.click()
    changePlanLoc =  "//div[@class='log_sec_price xl-12']/descendant::a"
    wait.until(ec.element_to_be_clickable((By.XPATH, changePlanLoc)))
    driver.find_element_by_xpath(changePlanLoc).click()
    el2 = driver.find_element_by_xpath("//div[@class='pricing_title_in_header']/child::h2")
    driver.refresh()
    wait.until(ec.staleness_of(el2))

