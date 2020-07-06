from base.find_element import FindElement
class LoginPage(object):
    def __init__(self,driver):
        self.fe = FindElement(driver)
    def get_phone_element(self):
        return self.fe.get_element('phone_num')
    def get_sms_code_element(self):
        return self.fe.get_element('sms_code')
    def get_login_btn(self):
        return self.fe.get_element('login_btn')

    def get_login_success_element(self):
        return self.fe.get_element('login_staff_name')