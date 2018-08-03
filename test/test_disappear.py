from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pages import page
#================== Variables ===========
link = 'https://www.vpnunlimitedapp.com/en/pricing'
subscriorin_type = "//a[@class='prices_cnt--item']"
change_plan_loc =  "//div[@class='log_sec_price xl-12']/descendant::a"
logo_path = "//div[@class='pricing_title_in_header']/child::h2"
#========================================
def test_disappeare(driver):
    disapear = page.PricingPage(driver)
    disapear.go_to_pricing(link)
    disapear.press_subscription(subscriorin_type)
    disapear.press_change_plan(change_plan_loc)
    disapear.wait_for_disappear(logo_path)
