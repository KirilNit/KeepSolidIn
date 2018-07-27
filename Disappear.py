from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get('https://www.vpnunlimitedapp.com/en/pricing')
#
wait = WebDriverWait(driver, 10)
# driver.refresh()
el1 = driver.find_element_by_xpath("//a[@class='prices_cnt--item']")
el1.click()
wait.until(ec.presence_of_element_located((By.XPATH, "//div[@class='pricing_title_in_header']/child::h2")))
el4 = driver.find_element_by_xpath("//div[@class='log_sec_price xl-12']/descendant::a")



'''
try:
    el3 = wait.until(ec.invisibility_of_element_located((By.XPATH,"//div[@class='pricing_title_in_header']/child::h2")))
except:
    print('Ni!')
finally:
    driver.quit()

    -------------
'''
try:
    el4.click() and WebDriverWait(driver, 10).until(ec.staleness_of(driver.find_element_by_xpath("//div[@class='pricing_title_in_header']/child::h2")))
    print('Disappeared')

except TimeoutException as ex:
    print('Exception')
finally:
    driver.quit()