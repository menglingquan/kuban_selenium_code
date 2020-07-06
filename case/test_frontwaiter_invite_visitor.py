from business.loginbusiness import LoginBusiness
from business.frontwaiter_invite_visitor_business import FrontWaiterInviteVisitorBusiness
from selenium import webdriver
from util.excel_util import ExcelUtil
import ddt
import time
import unittest
import os
import HTMLTestRunner
ex = ExcelUtil('D:\Kuban\config\waitervisitordata.xls')
data = ex.get_data()

@ddt.ddt
class FrontWaiterInviteVisitor(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://mgmt.ent-dev.kuban.io/')
        self.fivb = FrontWaiterInviteVisitorBusiness(self.driver)
        self.lb = LoginBusiness(self.driver)
    def tearDown(self) -> None:
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\image' + '\pic_' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
    @ddt.data(*data)
    def test_front_waiter_invite_nisitor(self,fivdata):
        phone, sms_code, visitor_name, visitor_email, visitor_phone, visitor_company, visitor_notes, suc_msg, name_error, email_error = fivdata
        self.lb.login_function(phone,sms_code)
        result = self.fivb.fronwaiterinvitevisitor(visitor_name,visitor_email,visitor_phone,visitor_company,visitor_notes,suc_msg,name_error,email_error)
        self.assertFalse(result,'over')
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\web_front_waiter_invite_visitor_report.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FrontWaiterInviteVisitor)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='报告', verbosity=2)
    runner.run(suite)