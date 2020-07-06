from business.loginbusiness import LoginBusiness
from business.admin_add_space_device_business import AdminAddSpaceDeviceBusiness
from selenium import webdriver
from util.excel_util import ExcelUtil
import time
import ddt
import unittest
import os
import HTMLTestRunner
ex = ExcelUtil('')
data = ex.get_data()
@ddt.ddt
class AdminAddSpaceDivice(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://mgmt.ent-dev.kuban.io/')
        self.lb = LoginBusiness(self.driver)
        self.asd = AdminAddSpaceDeviceBusiness(self.driver)

    def tearDown(self) -> None:
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\image' + '\pic_' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
    @ddt.data(*data)
    def test_admin_add_sapce_device(self,smdata):
        phone,sms_code = smdata
        self.lb.login_function(phone,sms_code)
        self.asd.admin_add_device()
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\webshayebushi_report.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(AdminAddSpaceDivice)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='ddt测试报告', description='ddt第一份哦', verbosity=2)
    runner.run(suite)