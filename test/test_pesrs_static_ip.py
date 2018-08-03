import allure
from allure.constants import AttachmentType
from pages import page

#==========Variables========

path = "//b[text()='Extras']"
check_url = 'https://www.vpnunlimitedapp.com/en/extras/personal-static-ip'
ip_xpath = "//a[@class='icon-font-arrow' and text()='Personal Static IP']"

#===========================

def test_ip(driver):
    """
    ===Description:
        -Go to 'https://www.vpnunlimitedapp.com/en'
        -Press 'Extras'
        -Click 'Personal Static IP'
    ===Expected Result:
        -'https://www.vpnunlimitedapp.com/en/extras/personal-static-ip' opening
    """

    ip = page.MainPage(driver)
    ip.go_to_main()
    ip.for_ip_extras(path)
    with allure.MASTER_HELPER.step('Screen_shot'):
        allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    ip.staticip_click(ip_xpath, check_url)
