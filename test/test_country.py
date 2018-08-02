from selenium.webdriver.common.keys import Keys
def test_cuntryinput(driver):
    """
    ===Description:
        -Go to 'https://www.vpnunlimitedapp.com/en/info/specials/server-locations'
        -Input country name with cyrillic chars
    ===Expected Result:
        -'Only latin characters and spaces are valid' warning appears under textfield
    """

    driver.get('https://www.vpnunlimitedapp.com/en/info/specials/server-locations')
    driver.find_element_by_xpath("//input[@id='server_countries_input']").send_keys('УкРаина')
    warning = driver.find_element_by_xpath\
        ("//span[text()='Only latin characters and spaces are valid']").text
    assert warning == 'Only latin characters and spaces are valid'