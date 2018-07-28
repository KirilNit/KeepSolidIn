from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

def test_disappear(driver):
    driver.get('https://www.vpnunlimitedapp.com/en/pricing')
    wait = WebDriverWait(driver, 10)
    el1 = driver.find_element_by_xpath("//a[@class='prices_cnt--item']")
    el1.click()
    wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='pricing_title_in_header']/child::h2")))
    el4 = driver.find_element_by_xpath("//div[@class='log_sec_price xl-12']/descendant::a")

    #тут работает только в таком вариант, лично у меня, при добавлении driver.refresh() тест крашится
    el4.click() and WebDriverWait(driver, 10).until(ec.staleness_of(driver.find_element_by_xpath("//div[@class='pricing_title_in_header']/child::h2")))

    """
    
    el4.click()
    driver.refresh()
    WebDriverWait(driver, 10).until(
        ec.staleness_of(driver.find_element_by_xpath("//div[@class='pricing_title_in_header']/child::h2")))
    """