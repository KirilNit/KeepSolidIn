from pages import page

incorrect_data = '234234dfsdf'
footer_inp = "//input[@class='footer_input_form']"
path = "//label[@class='footer_input_btn_label']"
path1 = "//div[@class='modal-popup--content']"
check_text = 'The "E-mail" field must contain a valid email address.'

def test_footerinpu(driver):
    """
    ===Description:
        -Go to 'https://www.vpnunlimitedapp.com/en'
        -Input incorrect data in Email-textfield in site footer with text 'Subscription'
        -Click to submit
    ===Expected Result:
        -'The "E-mail" field must contain a valid email address.' warning opens
    """

    footer = page.KeepSolidIn(driver)
    footer.go_to()
    footer.input_for_footer(incorrect_data, footer_inp )
    footer.click_for_footer(path, path1, check_text)
