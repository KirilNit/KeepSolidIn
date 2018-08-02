from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

def test_signine(driver):
    """
    ===Description:
        -Go to 'https://www.vpnunlimitedapp.com/en'
        -Open Navigation Bar
        -Press 'Sign In'
        -Enter Email as a login
        -Enter Password
        -Wait until you logined in
        -Open Navigation Bar
    ===Expected Result:
        -In navigation bar appears field 'My account'
    """
    driver.get('https://www.vpnunlimitedapp.com/en')
    wait = WebDriverWait(driver, 9)
    navBarr = driver.find_element_by_xpath("//label[@class='navbar-toggle']")
    navBarr.click()
    signInBut = wait.until(ec.element_to_be_clickable((By.XPATH,"//a[text()='Sign In']")))
    signInBut.click()
    emailfield = wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@class='user_login']/child::h4[text()='Email (KeepSolid ID)']/following-sibling::input")))
    passfield = wait.until(ec.element_to_be_clickable((By.XPATH,"//div[@class='log_sec_input ds-tab']/descendant::h4[text()='Password']/following-sibling::input[1]")))
    emailfield.send_keys('ForTestKeep@gmail.com')
    passfield.send_keys('1q2w3e4r5t')
    driver.find_element_by_xpath("//button[@class='l_s_login_btn button-find' and text()='Login']").click()
    time.sleep(6)
    navBarr.click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//a[text()='My account']")))
    driver.find_element_by_xpath("//a[text()='My account']").click()
