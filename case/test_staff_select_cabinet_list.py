from business.staff_select_cabinet_list_business import StaffSelectCabinetListBusiness
from business.loginbusiness import LoginBusiness
from util.excel_util import ExcelUtil
from selenium import webdriver
import ddt
import unittest
import os
import HTMLTestRunner
import time
ex = ExcelUtil()
data = ex.get_data()
@ddt.ddt
class StaffSelectCabinetList(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://mgmt.ent-dev.kuban.io/')
        self.scb = StaffSelectCabinetListBusiness(self.driver)
        self.lb = LoginBusiness(self.driver)
    def tearDown(self) -> None:
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\image' + '\pic_' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
    @ddt.data(*data)
    def test_staff_select_cabinet_list(self,datas):
        phone,sms_code = datas
        self.lb.login_function(phone,sms_code)
        result = self.scb.staff_select_cabinet_list_base()
        self.assertTrue(result,'一切正常，over')
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\web_staff_select_cabinet_report.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(StaffSelectCabinetList)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='ddt测试报告', description='ddt第一份哦', verbosity=2)
    runner.run(suite)