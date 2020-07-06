from business.loginbusiness import LoginBusiness
from business.location_admin_add_staff_business import LocationAdminAddStaffBusiness
from selenium import webdriver
from util.excel_util import ExcelUtil
import ddt
import time
import unittest
import os
import HTMLTestRunner
ex = ExcelUtil('D:\Kuban\config\staffdata.xls')
staff_data = ex.get_data()
@ddt.ddt
class LocationAdminAddStaff(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://mgmt.ent-dev.kuban.io/')
        self.lab = LocationAdminAddStaffBusiness(self.driver)
        self.lb = LoginBusiness(self.driver)
    def tearDown(self) -> None:
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd())+ '\image' + '\pic_' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
    @ddt.data(*staff_data)
    def test_loaction_admin_add_staff(self,ldata):
        phone, sms_code, staff_name,staff_job_number,staff_space_title,staff_phone_num,staff_email= ldata
        print(ldata)
        self.lb.login_function(phone,sms_code)
        result = self.lab.location_admin_add_staff(staff_name,staff_job_number,staff_space_title,staff_phone_num,staff_email)
        self.assertFalse(result,'123')
if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime())
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\web_report.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(LocationAdminAddStaff)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='报告', verbosity=2)
    runner.run(suite)