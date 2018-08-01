from selenium.webdriver.common.keys import Keys
def test_cuntryinput(driver):
    driver.get('https://www.vpnunlimitedapp.com/en/info/specials/server-locations')
    write = driver.find_element_by_xpath("//input[@id='server_countries_input']")
    write.send_keys('УкРаина')
    warning = driver.find_element_by_xpath\
        ("//span[text()='Only latin characters and spaces are valid']").text
    assert warning == 'Only latin characters and spaces are valid'