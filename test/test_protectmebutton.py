import allure
from allure.constants import AttachmentType
def test_protectee(driver):
    """
    ===Description:
        -Go to  'https://www.vpnunlimitedapp.com/en'
        -Press 'Protect Me'
    ===Expected Result:
        -Opening 'https://www.vpnunlimitedapp.com/en/downloads/windows'
    """
    driver.get('https://www.vpnunlimitedapp.com/en')
    driver.find_element_by_xpath("//a[text()='Protect Me']").click()
    with allure.MASTER_HELPER.step('Error'):
        allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    assert driver.current_url == 'https://www.vpnunlimitedapp.com/en/downloads/windows'
