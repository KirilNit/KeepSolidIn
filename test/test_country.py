from pages import page
import allure
from allure.constants import AttachmentType
#=======Variables=========
link = 'https://www.vpnunlimitedapp.com/en/info/specials/server-locations'
path_for_input = "//input[@id='server_countries_input']"
path_for_text = "//span[text()='Only latin characters and spaces are valid']"
#=========================
def test_cuntryinput(driver):
    """
    ===Description:
        -Go to 'https://www.vpnunlimitedapp.com/en/info/specials/server-locations'
        -Input country name with cyrillic chars
    ===Expected Result:
        -'Only latin characters and spaces are valid' warning appears under textfield
    """
    country = page.ServerLocation(driver)
    country.go_to_server_loc(link)
    with allure.MASTER_HELPER.step('Screen_shot'):
        allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    country.for_cyrillic_country(path_for_input, path_for_text)
