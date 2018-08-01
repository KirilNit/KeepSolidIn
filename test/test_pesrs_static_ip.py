from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
def test_ip(driver):
    driver.get('https://www.vpnunlimitedapp.com/en')
    wait = WebDriverWait(driver, 10)
    extras = driver.find_element_by_xpath("//b[text()='Extras']")
    extras.click()
    wait.until(ec.presence_of_element_located\
                   ((By.XPATH, "//a[@class='icon-font-arrow' and text()='Personal Static IP']")))
    driver.find_element_by_xpath\
        ("//a[@class='icon-font-arrow' and text()='Personal Static IP']").click()
    assert driver.current_url == 'https://www.vpnunlimitedapp.com/en/extras/personal-static-ip'