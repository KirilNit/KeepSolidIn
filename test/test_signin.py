import time
import allure
from allure.constants import AttachmentType
from pages import page
#=========Variables==========
navbar = "//label[@class='navbar-toggle']"
signin_button = "//a[text()='Sign In']"
email_path = "//div[@class='user_login']/child::h4[text()='Email (KeepSolid ID)']/following-sibling::input"
email = 'ForTestKeep@gmail.com'
pass_path = "//div[@class='log_sec_input ds-tab']/descendant::h4[text()='Password']/following-sibling::input[1]"
password = '1q2w3e4r5t'
login_but = "//button[@class='l_s_login_btn button-find' and text()='Login']"
my_acc = "//a[text()='My account']"
#============================
def test_signine(driver):
    """
    ===Description:
        -Go to 'https://www.vpnunlimitedapp.com/en'
        -Open Navigation Bar
        -Press 'Sign In'
        -Enter Email as a login
        -Enter Password
        -Wait until you logined in
        -Open Navigation Bar
    ===Expected Result:
        -In navigation bar appears field 'My account'
    """

    login = page.MainPage(driver)
    login.go_to_main()
    login.click_for_signin(navbar)
    login.sign_in_press(signin_button)
    login.enter_email(email_path, email)
    login.enter_pass(pass_path, password)
    with allure.MASTER_HELPER.step('Screen_shot_input'):
        allure.MASTER_HELPER.attach('screen_shot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    login.click_for_signin(login_but)
    time.sleep(6)
    login.click_for_signin(navbar)
    login.sign_in_press(my_acc)
