from business.loginbusiness import LoginBusiness
from business.add_munberbusiness import AddMenBusiness
from selenium import webdriver
import time
import ddt
import unittest
import os
import HTMLTestRunner
from util.excel_util import ExcelUtil
amex = ExcelUtil('D:\Kuban\config\mendata.xls')
login_data = amex.get_data()

@ddt.ddt
class AddMen(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        # self.driver.maximize_window()
        self.driver.get('https://mgmt.ent-dev.kuban.io/')

        self.amb = AddMenBusiness(self.driver)
        self.lb = LoginBusiness(self.driver)

    def tearDown(self):
        for method_name, error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\image' + '\pic_' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()

    @ddt.data(*login_data)
    def test_add_men(self,mendata):
        phone, sms_code, menName,menID,sapceTitle,menPhone,menEmail= mendata
        self.lb.login_function(phone, sms_code)
        time.sleep(3)
        self.amb.add_men_function(menName,menID,sapceTitle,menPhone,menEmail)
        time.sleep(3)


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\web_add_men_report.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(AddMen)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='ddt测试报告',description='ddt第一份哦',verbosity=2)
    runner.run(suite)