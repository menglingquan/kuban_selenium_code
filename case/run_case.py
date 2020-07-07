import unittest
import os
import HTMLTestRunner
class RunCase(unittest.TestCase):
    def text_case01(self):
        case_path = os.path.join(os.getcwd())
        print(case_path)
        suite = unittest.defaultTestLoader.discover(case_path,'test*.py')
        print(suite)
        #unittest.TextTestRunner().run(suite)
        f = open('D://Kuban//webreport//rrrrrt.html', 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='ddt测试报告', description='ddt第一份哦', verbosity=2)
        runner.run(suite)
if __name__ == '__main__':
    RunCase().text_case01()
