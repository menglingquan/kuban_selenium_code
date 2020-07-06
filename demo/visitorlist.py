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
        driver.find_element_by_id('phone_num').send_keys(phone)
        time.sleep(2)
        driver.find_element_by_id('login_sms_code').send_keys(sms_code)
        driver.find_element_by_xpath(
            '//*[@id="root"]/div/div/div/form/div/div/div[2]/div[2]/div/div/span/button').click()
        time.sleep(16)
        driver.find_element_by_xpath('//*[@id="sider"]/div/ul/li[4]/div').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="/locations/visitor$Menu"]/li[2]').click()
        time.sleep(2)
        #访客名称搜索
        driver.find_element_by_xpath('//input[@type="text"]').send_keys(visitor_name)
        time.sleep(2)
        #获取访客列表第一个访客名称
        select_result= driver.find_element_by_class_name('antd-pro-pages-visitor-components-visitor-avatar-visitorNames').text
        print(select_result)
        #清空搜索框
        driver.find_element_by_xpath('//input[@type="text"]').clear()
        time.sleep(1)
        #访客详情
        driver.find_element_by_class_name('antd-pro-pages-visitor-components-visitor-avatar-visitorNames').click()
        time.sleep(1)
        #访客访客列表
        driver.find_element_by_class_name('skipRouterHeader').click()
        time.sleep(1)
        #获取第一个访客姓名
        name = driver.find_element_by_class_name('antd-pro-pages-visitor-components-visitor-avatar-visitorNames').text
        print(name)
        #导出报表
        driver.find_element_by_xpath('//*[@class="antd-pro-components-page-header-index-action"]/div/div/button').click()
        time.sleep(0.5)
        hhh = driver.find_element_by_class_name('ant-message').text
        print(hhh)
        #日期筛选
        driver.find_element_by_class_name('antd-pro-components-date-picker-with-arrows-index-arrowbtn').click()
        time.sleep(2)
        driver.close()
if __name__ == '__main__':
    unittest.main()