from base.find_element import FindElement
class FirstPage(object):
    def __init__(self,driver):
        self.fe = FindElement(driver)
    def get_phone_element(self):
        return self.fe.get_element('login_phone')
    def get_phone_error_element(self):
        return self.fe.get_element('phone_error')
    def get_login_btn(self):
        return self.fe.get_element('login_btn')