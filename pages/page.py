from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver


class KeepSolidIn:
    def __init__(self, driver):
        self.driver = driver


    def go_to(self, link = 'https://www.vpnunlimitedapp.com/en'):
        self.driver.get(link)
        return self

    '''
    def screen(self): 
        '''

    def for_cyrillic_country(self, path, pah2):
        self.driver.find_element_by_xpath(path).send_keys('УкРаина')
        assert self.driver.find_element_by_xpath(pah2).text == 'Only latin characters and spaces are valid'


    def input_for_footer(self, incorrect_data, path):
        self.driver.find_element_by_xpath(path).send_keys(incorrect_data)


    def click_for_footer(self, path, path1, check_text):
        self.driver.find_element_by_xpath(path).click()
        wait = WebDriverWait(self.driver, 9)
        wait.until(ec.presence_of_element_located((By.XPATH, path1)))
        assert self.driver.find_element_by_xpath("//p[@class='form-error']").text == check_text


    def for_ip_extras(self,path):

        self.driver.find_element_by_xpath(path).click()


    def staticip_click(self,ip_xpath, check_url):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located \
                       ((By.XPATH, ip_xpath)))
        self.driver.find_element_by_xpath \
            (ip_xpath).click()
        assert self.driver.current_url == check_url


    def protect_me(self, button, check_link):
        self.driver.find_element_by_xpath(button).click()
        assert self.driver.current_url == check_link


    def click_for_signin(self, path):
        self.driver.find_element_by_xpath(path).click()


    def sign_in_press(self, path):
        wait = WebDriverWait(self.driver, 9)
        wait.until(ec.element_to_be_clickable((By.XPATH, path)))
        self.driver.find_element_by_xpath(path).click()

    def enter_email(self, email_path, email):
        wait = WebDriverWait(self.driver, 9)
        wait.until(ec.element_to_be_clickable((By.XPATH, email_path)))
        self.driver.find_element_by_xpath(email_path).send_keys(email)

    def enter_pass(self, pass_path, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH,pass_path)))
        self.driver.find_element_by_xpath(pass_path).send_keys(password)