from business.loginbusiness import LoginBusiness
from business.location_admin_add_activity_business import LocationAdminAddActivityBusiness
from selenium import webdriver
from util.excel_util import ExcelUtil
import ddt
import time
import unittest
import os
import HTMLTestRunner
ex = ExcelUtil('D:\Kuban\config\locationactivities.xls')
data = ex.get_data()
print(data)
@ddt.ddt
class Fwhta(unittest.TestCase):
    @ddt.data(*data)
    def test_eeee(self,fivdata):
        phone, sms_code, activity_title, activity_space, activity_ticket, activity_note, pic_path = fivdata
        print(phone, sms_code, activity_title, activity_space, activity_ticket, activity_note, pic_path)
        driver = webdriver.Chrome()
        driver.get('https://mgmt.ent-dev.kuban.io/')
        driver.find_element_by_id('phone_num').send_keys('17600909177')
        time.sleep(2)
        driver.find_element_by_id('login_sms_code').send_keys('123456')
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div/form/div/div/div[2]/div[2]/div/div/span/button').click()
        time.sleep(13)
        driver.find_element_by_xpath('//*[@class="ant-layout-sider-children"]/ul/li[8]').click()
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//*[@id="/locations/activity$Menu"]/li').click()
            time.sleep(1)
        except:
            print('meizhaodao')
        driver.find_element_by_xpath('//button[@type="button"]').click()
        time.sleep(2)
        # driver.find_element_by_id('title').send_keys('selenium活动标题')
        # driver.find_element_by_id('activity_type_id').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('//*[@role="listbox"]/li').click()
        # time.sleep(1)
        # driver.find_element_by_id('activityTime').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('//*[@class="ant-calendar-date-panel"]/div[2]/div[2]/div[2]/table/tbody/tr/td').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('//*[@class="ant-calendar-date-panel"]/div[2]/div[2]/div[2]/table/tbody/tr[6]/td').click()
        # time.sleep(1)
        # driver.find_element_by_class_name('ant-calendar-ok-btn').click()
        # time.sleep(2)
        a = r'C:\Users\HUAWEI\Desktop\p60211809.jpg'
        print(pic_path)
        print(a)
        driver.find_element_by_xpath('//input[@type="file"]').send_keys(pic_path)
        time.sleep(5)
        # driver.find_element_by_xpath('//*[@id="ticket_end_date"]/div/input').click()
        # time.sleep(1)
        # driver.find_element_by_class_name('ant-calendar-next-month-btn').click()
        # time.sleep(1)
        # driver.find_element_by_xpath('//*[@class="ant-calendar-tbody"]/tr[2]/td[5]').click()
        # time.sleep(2)
        # driver.find_element_by_id('address').send_keys('北京市朝阳区')
        # driver.find_element_by_id('tickets').send_keys('12')
        # driver.find_element_by_xpath('//*[@id="prioritized"]/label[2]/span/input').click()
        # time.sleep(3)
        driver.find_element_by_xpath('//div[@aria-label="rdw-editor"]').send_keys('selenium活动内容')
        # time.sleep(2)
        # driver.find_element_by_xpath('//*[@class="antd-pro-components-page-header-index-action"]/div/button[2]').click()
        time.sleep(5)

        driver.close()
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    file_path = os.path.abspath(os.path.dirname(os.getcwd()) + '\webreport' + '\web_report.html')
    f = open(file_path, 'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(Fwhta)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='ddt测试报告', description='ddt第一份哦', verbosity=2)
    runner.run(suite)