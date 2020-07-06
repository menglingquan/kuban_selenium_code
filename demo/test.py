from util.excel_util import ExcelUtil
import unittest
import ddt
ex = ExcelUtil('D:\Kuban\config\staffdata.xls')
data = ex.get_data()
@ddt.ddt
class emmm(unittest.TestCase):

    def setUp(self):
        print('setup')


    def tearDown(self):
        print('teardown')
    @ddt.data(*data)
    def test001(self,data):
        print(data)
        print(type(data))
        print('teardown')

    @ddt.data(*data)
    def test0013(self, data):
        print(data)

    def test002(self):
        print('22222222222222222222')

if __name__ == '__main__':
    unittest.main()