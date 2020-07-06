import unittest
import time
import os
import HTMLTestRunner
class FirstCase01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('这是01所有的前置')
    @classmethod
    def tearDownClass(cls):
        print('这是01所有的后置')


    def setUp(self) :
        print('这是01case前置条件')

    def tearDown(self):
        print('这是01case后置条件')
    @unittest.skip('这是01第一条不执行')
    def test_first01(self):
        print('这是01第一条case')
    def test_first02(self):
        a = False
        if a == True:
            print('121323')
        else:
            print('!!!')

if __name__ == '__main__':
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    # file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\web_'+now+'report.html')
    f = open('D://Kuban//webreport//rtttt.html', 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase01)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='ddt测试报告', description='ddt第一份哦', verbosity=2)
    runner.run(suite)