from selenium import webdriver
from util.excel_util import ExcelUtil
import time
import unittest
import ddt
ex = ExcelUtil('D:\Kuban\config\svisitordata.xls')
data = ex.get_data()
@ddt.ddt
class lalalal(unittest.TestCase):
    @ddt.data(*data)
    def test_hahha(self,xdata):
        phone, sms_code, visitor_name, visitor_email, visitor_phone, visitor_company, visitor_notes, suc_msg, name_error, email_error = xdata
        print(xdata)
        driver = webdriver.Chrome()
        driver.get('https://mgmt.ent-dev.kuban.io/')
        driver.find_element_by_id('phone_num').send_keys('19934893589')
        time.sleep(2)
        driver.find_element_by_id('login_sms_code').send_keys(sms_code)
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/form/div/div/div[2]/div[2]/div/div/span/button').click()
        time.sleep(16)



        #进入访客模块
        driver.find_element_by_xpath('//*[@id="sider"]/div/ul/li[4]/div').click()
        time.sleep(2)
        #查看访客列表
        driver.find_element_by_xpath('//*[@id="/locations/visitor$Menu"]/li[2]').click()
        time.sleep(2)
        #获取第一个访客的详情
        driver.find_element_by_class_name('antd-pro-pages-visitor-components-visitor-avatar-visitorNames').click()
        time.sleep(1)
        #同意审批
        try:
            driver.find_element_by_xpath('//*[@class="ant-drawer-body"]/div/div/div/div/button').click()
            time.sleep(1)
            driver.find_element_by_xpath(
                '//*[@class="ant-table-row ant-table-row-level-0"]/div/div/div/div/button').click()
            time.sleep(2)
        except:
            driver.find_element_by_class_name('skipRouterHeader').click()
            time.sleep(2)
            print('不需要审批哦')
        # 全选
        driver.find_element_by_class_name('ant-checkbox-input').click()
        # 批量审批
        driver.find_element_by_xpath('//*[@class="visitor"]/div/button[3]').click()
        time.sleep(3)
        #获取第一个访客的签到按钮
        #确定签到
        try:
            driver.find_element_by_xpath('//*[@class="ant-table-tbody"]/tr/td/button').click()
            time.sleep(5)
            driver.find_element_by_xpath('//*[@class="ant-modal-footer"]/div/button[2]').click()
            time.sleep(5)
        except:
            print('已经签到过了呢')

        #全选
        driver.find_element_by_class_name('ant-checkbox-input').click()
        # 批量签到
        driver.find_element_by_xpath('//*[@class="visitor"]/div/button').click()
        #签退
        try:
            driver.find_element_by_xpath('//*[@class="ant-table-tbody"]/tr/td/button').click()
            time.sleep(5)
        except:
            print('已经签退过了呢')
        # 全选
        driver.find_element_by_class_name('ant-checkbox-input').click()
        # 批量签退
        driver.find_element_by_xpath('//*[@class="visitor"]/div/button[2]').click()
        #点击更多
        #删除访客
        #确认删除
        driver.find_element_by_xpath('//*[@class="ant-table-fixed-right"]/div/div/table/tbody/tr/td/div/i').click()
        driver.find_element_by_xpath('//*[@class="ant-popover-inner-content"]/div/span[4]/i').click()
        driver.find_element_by_xpath('//*[@class="ant-popover-buttons"]/button[2]').click()
        time.sleep(4)
        # 签退
        driver.close()
        #批量签退
if __name__ == '__main__':
    unittest.main()