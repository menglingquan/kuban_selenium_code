from business.staff_book_desk_businsess import StaffBookDeskBusiness
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
class StaffBookDesk(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://mgmt.ent-dev.kuban.io/')
        self.sdb = StaffBookDeskBusiness(self.driver)
        self.lb = LoginBusiness(self.driver)
    def tearDown(self):
        for menthod_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\image' + '\pic_' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
    @ddt.data(*data)
    def test_staff_book_desk(self,ldata):
        phone, sms_code = ldata
        self.lb.login_function(phone,sms_code)
        result = self.sdb.staff_book_desk()
        self.assertTrue(result,'判断是否找到预定成功提示语')
if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime())
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\web_report'+now+'.html')
    f = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(StaffBookDesk)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='测试报告',description='工位的',verbosity=2)
    runner.run(suite)