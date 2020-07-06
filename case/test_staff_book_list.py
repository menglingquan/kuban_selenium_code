from business.staff_book_list_business import StaffBookListBusiness
from business.loginbusiness import LoginBusiness
from selenium import webdriver
from util.excel_util import ExcelUtil
import time
import ddt
import unittest
import os
import HTMLTestRunner
ex = ExcelUtil()
data = ex.get_data()
@ddt.ddt
class StaffBookList(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://mgmt.ent-dev.kuban.io/')
        self.slb = StaffBookListBusiness(self.driver)
        self.lb = LoginBusiness(self.driver)
    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\image' + '\pic_' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
    @ddt.data(*data)
    def test_staff_book_list(self,ldata):
        phone, sms_code = ldata
        self.lb.login_function(phone, sms_code)
        time.sleep(13)
        result = self.slb.staff_book_list()
        self.assertTrue(result,'成功')
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\web_report.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(StaffBookList)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='ddt测试报告',description='ddt第一份哦',verbosity=2)
    runner.run(suite)