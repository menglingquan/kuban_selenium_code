from business.loginbusiness import LoginBusiness
from selenium import webdriver
import time
import ddt
import unittest
import os
import HTMLTestRunner
from util.excel_util import ExcelUtil
ex = ExcelUtil()
data = ex.get_data()
@ddt.ddt
class LoginCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get('https://mgmt.ent-dev.kuban.io/')
        self.lb = LoginBusiness(self.driver)

    def tearDown(self):
         for method_name, error in self._outcome.errors:
             if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport'+'\T'+case_name + '.png')
                self.driver.save_screenshot(file_path)
         self.driver.close()
    #手机号    错误信息定位元素     错误信息提示
    # @ddt.data(
    #         ['123123','phone_error','百度一下'],
    #         ['111','phone_error','百度一下']
    #     )

    # @ddt.unpack
    @ddt.data(*data)
    def test_login(self,ldata):
        phone, sms_code= ldata
        login_success_msg = self.lb.login_function(phone,sms_code)
        self.assertTrue(login_success_msg,'登录成功')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\web_login_report.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='ddt测试报告',description='ddt第一份哦',verbosity=2)
    runner.run(suite)