from handle.firsthandle import FirstHandle
import time
class FirstBusiness(object):
    def __init__(self,driver):
        self.fh = FirstHandle(driver)
    def login_base(self,phone):
        self.fh.send_phone_value(phone)
        self.fh.click_login_button()

    def login_success(self,phone):
        self.login_base(phone)
        if self.fh.get_msg('phone_error','百度一下'):
            print('登陆成功信息检测不成功')
            return True
        else:
            print('登陆成功信息检测成功')
            return False
    def login_phone_error(self,phone):
        self.login_base(phone)
        #self.fh.get_msg()
        if self.fh.get_msg('phone_error','百度一下'):
            print('错误手机号检测不成功')
            return True
        else:
            print('错误手机号检测成功')
            return False

    def login_function(self,phone,assertCode,assertText):
        self.login_base(phone)
        if self.fh.get_msg(assertCode, assertText) == None:
            print('错误手机号检测不成功')
            return True
        else:
            print('错误手机号检测成功')
            return False