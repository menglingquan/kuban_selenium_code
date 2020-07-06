from business.firstbusiness import FirstBusiness
from selenium import webdriver
from log.user_log import UserLog
import time
import unittest
import os
import HTMLTestRunner


class FirstCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.log = UserLog()
        cls.logger = cls.log.get_log()
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.baidu.com')
        self.logger.info('this is chrome')

        self.fb = FirstBusiness(self.driver)
    def tearDown(self) :
        for method_name,error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\image' +'\pic_'+case_name+ '.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()

    def test_login_phone_error(self):
        phone_error = self.fb.login_phone_error('123213')
        time.sleep(3)
        # self.assertFalse(phone_error,'登录失败，用例成功')
        self.assertFalse(phone_error,'登录成功，用例失败')
        # if phone_error  == True:
        #     print('登录成功，用例失败')
        # else:
        #     print('登录失败，用例成功')

    def test_login_success(self):
        success = self.fb.login_success('123213')
        time.sleep(3)
        if success == True:
            print('登录失败，用例失败')
        else:
            print('登录成功，用例成功')


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\web_report.html')
    print(file_path)
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FirstCase('test_login_phone_error'))
    suite.addTest(FirstCase('test_login_success'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='测试报告',description='第一份哦',verbosity=2)
    runner.run(suite)
