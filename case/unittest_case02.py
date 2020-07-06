import unittest
import time
import os
import HTMLTestRunner

class FirstCase02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('这是02所有的前置')
    @classmethod
    def tearDownClass(cls):
        print('这是02所有的后置')


    def setUp(self) :
        print('这是02case前置条件')

    def tearDown(self):
        print('这是02case后置条件')

    def test_first01(self):
        print('这是caseo2的第一条case')

    @unittest.skip('这是case01的第一条不执行')
    def test_first02(self):
        print('这是caseo2的第二条case')
if __name__ == '__main__':
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    # file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '/webreport' + '/web_888888report.html')
    f = open('D://Kuban//webreport//rrrrrt.html', 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase02)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='ddt测试报告', description='ddt第一份哦', verbosity=2)
    runner.run(suite)