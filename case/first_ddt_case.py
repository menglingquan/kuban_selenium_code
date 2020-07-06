from business.firstbusiness import FirstBusiness
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
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')
        self.fb = FirstBusiness(self.driver)

    def tearDown(self):
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\image' + '\pic_' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
    #手机号    错误信息定位元素     错误信息提示
    # @ddt.data(
    #         ['123123','phone_error','百度一下'],
    #         ['111','phone_error','百度一下']
    #     )
    # @ddt.unpack
    @ddt.data(*data)
    def test_login(self,data):
        phone, assertCode, assertText = data
        phone_error = self.fb.login_function(phone,assertCode,assertText)
        time.sleep(3)
        self.assertFalse(phone_error,'登录成功，用例失败')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\web_report.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='ddt测试报告',description='ddt第一份哦',verbosity=2)
    runner.run(suite)