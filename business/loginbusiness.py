from handle.loginhandle import LoginHandle
import time
class LoginBusiness(object):
    def __init__(self,driver):
        self.lh = LoginHandle(driver)
    def login_base(self,phone,sms_code):
        self.lh.send_phone_value(phone)
        time.sleep(1)
        self.lh.send_sms_code_value(sms_code)
        self.lh.click_login_button()

    def login_success(self,phone):
        self.login_base(phone)
        time.sleep(0.3)
        if self.lh.get_msg('phone_error_msg','电话或验证码错误') == None:
            print('登陆成功')
            return True
        else:
            print('登陆失败')
            return False
    def login_phone_error(self,phone):
        self.login_base(phone)
        if self.lh.get_msg('phone_error_msg','请输入手机号格式错误') == None:
            print('错误手机号检测不成功')
            return True
        else:
            print('错误手机号检测成功')
            return False

    def login_function(self,phone,sms_code):
        self.login_base(phone,sms_code)
        time.sleep(10)
        if self.lh.get_login_success_msg() == None:
            return False
        return False
        # if self.lh.get_msg(assertCode, assertText) == None:
        #     print('登录成功')
        #     return True
        #
        # return False
