from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages import page

#=====================

path = "//b[text()='Extras']"
check_url = 'https://www.vpnunlimitedapp.com/en/extras/personal-static-ip'
ip_xpath = "//a[@class='icon-font-arrow' and text()='Personal Static IP']"

#=====================

def test_ip(driver):
    """
    ===Description:
        -Go to 'https://www.vpnunlimitedapp.com/en'
        -Press 'Extras'
        -Click 'Personal Static IP'
    ===Expected Result:
        -'https://www.vpnunlimitedapp.com/en/extras/personal-static-ip' opening
    """

    ip = page.KeepSolidIn(driver)
    ip.go_to()
    ip.for_ip_extras(path)
    ip.staticip_click(ip_xpath, check_url)
