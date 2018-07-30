from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver
def test_footerInp(driver):
    driver.get('https://www.vpnunlimitedapp.com/en')
    inpForm = driver.find_element_by_xpath("//input[@class='footer_input_form']")
    inpForm.send_keys('234234dfsdf')
    label = driver.find_element_by_xpath("//label[@class='footer_input_btn_label']")
    label.click()
    wait = WebDriverWait(driver, 11)
    wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='modal-popup--content']")))
    errorattr = driver.find_element_by_xpath("//p[@class='form-error']").text
    assert errorattr != 'The "E-mail" field is required.'