from business.loginbusiness import LoginBusiness
from business.location_admin_add_activity_business import LocationAdminAddActivityBusiness
from selenium import webdriver
from util.excel_util import ExcelUtil
import ddt
import time
import unittest
import os
import HTMLTestRunner
ex = ExcelUtil('D:\Kuban\config\locationactivities.xls')
data = ex.get_data()

@ddt.ddt
class LocationAdminAddActivity(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://mgmt.ent-dev.kuban.io/')
        self.laab = LocationAdminAddActivityBusiness(self.driver)
        self.lb = LoginBusiness(self.driver)
    def tearDown(self) -> None:
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\image' + '\pic_' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
    @ddt.data(*data)
    def test_location_admin_add_activity(self,fivdata):
        phone, sms_code, activity_title, activity_space, activity_ticket, activity_note, pic_path = fivdata
        self.lb.login_function(phone,sms_code)
        result = self.laab.add_activity( activity_title, activity_space, activity_ticket, activity_note, pic_path)
        self.assertFalse(result,'over')
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\web_front_waiter_invite_visitor_report.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(LocationAdminAddActivity)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='报告', verbosity=2)
    runner.run(suite)