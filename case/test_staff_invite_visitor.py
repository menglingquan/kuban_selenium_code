from business.loginbusiness import LoginBusiness
from business.staff_invite_visitor_business import StaffInviteVisitorBusiness
from selenium import webdriver
from util.excel_util import ExcelUtil
import time
import ddt
import unittest
import os
import HTMLTestRunner
ex = ExcelUtil('D:\Kuban\config\svisitordata.xls')
data = ex.get_data()

@ddt.ddt
class StaffInviteVisitor(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://mgmt.ent-dev.kuban.io/')
        self.ivb = StaffInviteVisitorBusiness(self.driver)
        self.lb = LoginBusiness(self.driver)
    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\image' + '\pic_' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
    @ddt.data(*data)
    def test_staff_invite_visitor(self,ivdata):
        phone,sms_code,visitor_name,visitor_email,visitor_phone,visitor_company,visitor_notes,suc_msg,name_error,email_error = ivdata
        self.lb.login_function(phone,sms_code)
        result = self.ivb.staff_invite_visitor_base(visitor_name,visitor_email,visitor_phone,visitor_company,visitor_notes,suc_msg,name_error,email_error)
        self.assertTrue(result,'成功')
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\web_staff_invite_visitor_report.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(StaffInviteVisitor)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='ddt测试报告', description='ddt第一份哦', verbosity=2)
    runner.run(suite)