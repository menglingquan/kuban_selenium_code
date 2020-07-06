from business.Staff_book_meeting_business import StaffBookMeetingBusiness
from business.loginbusiness import LoginBusiness
from selenium import webdriver
from util.excel_util import ExcelUtil
import time
import ddt
import unittest
import os
import HTMLTestRunner
ex = ExcelUtil('D:\Kuban\config\staffbookroom.xls')
data = ex.get_data()
@ddt.ddt
class StaffBookMeeting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://mgmt.ent-dev.kuban.io/')
        self.smb = StaffBookMeetingBusiness(self.driver)
        self.lb = LoginBusiness(self.driver)
    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd())  + '\image' + '\pic_' + case_name + '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()
    @ddt.data(*data)
    def test_staff_book_meeting(self,smdata):
        phone,sms_code,meeting_theme,meeting_issue = smdata
        self.lb.login_function(phone,sms_code)
        time.sleep(15)
        self.smb.StaffBookMeetingBusiness_base(meeting_theme,meeting_issue)
        time.sleep(2)
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\web_staff_book_meet_report.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(StaffBookMeeting)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='ddt测试报告', description='ddt第一份哦', verbosity=2)
    runner.run(suite)