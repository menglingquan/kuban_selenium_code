from page.firstpage import FirstPage
class FirstHandle(object):
    def __init__(self,driver):
        self.fp = FirstPage(driver)
    def send_phone_value(self,phone):
        self.fp.get_phone_element().send_keys(phone)

    def click_login_button(self):
        self.fp.get_login_btn().click()

    def get_msg(self,info,msg_info):
        try:
            if info == 'phone_error':
                text = self.fp.get_phone_error_element().text
        except:
            text = None
        return text