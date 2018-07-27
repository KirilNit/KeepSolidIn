'''from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import time'''
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait



def test_visible(driver):
    driver.get('https://www.vpnunlimitedapp.com/en')
    plBut = driver.find_element_by_xpath("//div[@class='pulse2']/ancestor::a")


    wait = WebDriverWait(driver, 10)
    plBut.click()
    #driver.refresh()
    wait.until(ec.visibility_of(driver.find_element_by_xpath("//video")))
