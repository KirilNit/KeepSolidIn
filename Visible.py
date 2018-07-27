from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
driver.get('https://www.vpnunlimitedapp.com/en')

plBut = driver.find_element_by_xpath("//div[@class='pulse2']/ancestor::a")
plBut.click()

wait = WebDriverWait(driver, 10)
try:
    wait.until(ec.visibility_of(driver.find_element_by_xpath("//video")))
    time.sleep(25)
except TimeoutException:
    print('Ni!')
finally:
    driver.quit()