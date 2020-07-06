import ddt
import unittest
@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print('setup')
    def tearDown(self):
        print('teardown')
    #手机号、验证码
    @ddt.data(
        ['错误手机号'],
        ['正确手机号']
    )

    @ddt.unpack
    def test_add(self,a):
        print(a)
if __name__ == '__main__':
    unittest.main()