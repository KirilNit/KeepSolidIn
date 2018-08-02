from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver
def test_footerinpu(driver):
    """
    ===Description:
        -Go to 'https://www.vpnunlimitedapp.com/en'
        -Input incorrect data in Email-textfield in site footer with text 'Subscription'
    ===Expected Result:
        -'The "E-mail" field must contain a valid email address.' warning opens
    """
    driver.get('https://www.vpnunlimitedapp.com/en')
    driver.find_element_by_xpath("//input[@class='footer_input_form']").send_keys('234234dfsdf')
    driver.find_element_by_xpath("//label[@class='footer_input_btn_label']").click()
    wait = WebDriverWait(driver, 9)
    wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='modal-popup--content']")))
    assert driver.find_element_by_xpath("//p[@class='form-error']").text == 'The "E-mail" field must contain' \
                                                                            ' a valid email address.'