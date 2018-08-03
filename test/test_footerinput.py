from pages import page
import allure
from allure.constants import AttachmentType
#========Variables===========
incorrect_data = '234234dfsdf'
footer_inp = "//input[@class='footer_input_form']"
path = "//label[@class='footer_input_btn_label']"
path1 = "//div[@class='modal-popup--content']"
check_text = 'The "E-mail" field must contain a valid email address.'
#============================
def test_footerinpu(driver):
    """
    ===Description:
        -Go to 'https://www.vpnunlimitedapp.com/en'
        -Input incorrect data in Email-textfield in site footer with text 'Subscription'
        -Click to submit
    ===Expected Result:
        -'The "E-mail" field must contain a valid email address.' warning opens
    """

    footer = page.MainPage(driver)
    footer.go_to_main()
    footer.input_for_footer(incorrect_data, footer_inp )
    with allure.MASTER_HELPER.step('Screen_shot'):
        allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    footer.click_for_footer(path, path1, check_text)
