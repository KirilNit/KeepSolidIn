from pages import page
link = 'https://www.vpnunlimitedapp.com/en/info/specials/server-locations'
path_for_input = "//input[@id='server_countries_input']"
path_for_text = "//span[text()='Only latin characters and spaces are valid']"
def test_cuntryinput(driver):
    """
    ===Description:
        -Go to 'https://www.vpnunlimitedapp.com/en/info/specials/server-locations'
        -Input country name with cyrillic chars
    ===Expected Result:
        -'Only latin characters and spaces are valid' warning appears under textfield
    """
    country = page.KeepSolidIn(driver)
    country.go_to(link)
    country.for_cyrillic_country(path_for_input, path_for_text)
