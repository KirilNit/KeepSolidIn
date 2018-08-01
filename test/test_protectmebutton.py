def test_protecte(driver):
    driver.get('https://www.vpnunlimitedapp.com/en')
    button = driver.find_element_by_xpath("//a[text()='Protect Me']")
    button.click()
    page = driver.current_url
    assert page == 'https://www.vpnunlimitedapp.com/en/downloads/windows'
