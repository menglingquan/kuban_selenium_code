from page.loginpage import LoginPage
import time
class LoginHandle(object):
    def __init__(self,driver):
        self.lp = LoginPage(driver)
    def send_phone_value(self,phone):
        self.lp.get_phone_element().send_keys(phone)
    def send_sms_code_value(self,sms_code):
        self.lp.get_sms_code_element().send_keys(sms_code)
    def click_login_button(self):
        self.lp.get_login_btn().click()
        time.sleep(10)
    def get_login_success_msg(self):
        try:
            login_success = self.lp.get_login_success_element().text
        except:
            login_success = None
        return login_success
    #     try:
    #         if info == 'phone_error_msg':
    #             text = self.lp.get_phone_error_element().text
    #         # if info == 'sms_code_error':
    #         #     text = self.lp.get_sms_code_error_element().text
    #     except:
    #         text = None
    #     return text