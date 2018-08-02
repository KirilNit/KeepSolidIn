from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
def test_ip(driver):
    """
    ===Description:
        -Go to 'https://www.vpnunlimitedapp.com/en'
        -Press 'Extras'
        -Click 'Personal Static IP'
    ===Expected Result:
        -'https://www.vpnunlimitedapp.com/en/extras/personal-static-ip' opening
    """

    driver.get('https://www.vpnunlimitedapp.com/en')
    wait = WebDriverWait(driver, 10)
    driver.find_element_by_xpath("//b[text()='Extras']").click()
    wait.until(ec.presence_of_element_located\
                   ((By.XPATH, "//a[@class='icon-font-arrow' and text()='Personal Static IP']")))
    driver.find_element_by_xpath\
        ("//a[@class='icon-font-arrow' and text()='Personal Static IP']").click()
    assert driver.current_url == 'https://www.vpnunlimitedapp.com/en/extras/personal-static-ip'