import allure
from allure.constants import AttachmentType
from pages import  page

button_me = "//a[text()='Protect Me']"
check_link = 'https://www.vpnunlimitedapp.com/en/downloads/windows'

def test_protectee(driver):
    """
    ===Description:
        -Go to  'https://www.vpnunlimitedapp.com/en'
        -Press 'Protect Me'
    ===Expected Result:
        -Opening 'https://www.vpnunlimitedapp.com/en/downloads/windows'
    """

    button = page.KeepSolidIn(driver)
    button.go_to()
    with allure.MASTER_HELPER.step('Error'):
        allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    button.protect_me(button_me, check_link)
