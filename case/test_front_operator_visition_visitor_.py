from business.loginbusiness import LoginBusiness
from business.front_operation_visitor_business import FrontOperationVisitorBusiness
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
class FrontOperationVisitor(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://mgmt.ent-dev.kuban.io/')
        self.lb = LoginBusiness(self.driver)
        self.fovb = FrontOperationVisitorBusiness(self.driver)

    def tearDown(self) -> None:
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\image' + '\pic_' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
    @ddt.data(*data)
    def test_front_operatin_visitor(self,smdata):
        phone,sms_code = smdata
        self.lb.login_function(phone,sms_code)
        self.fovb.frontoperationvisitor()
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\web_front_operation_visitor_report.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FrontOperationVisitor)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='ddt测试报告', description='ddt第一份哦', verbosity=2)
    runner.run(suite)