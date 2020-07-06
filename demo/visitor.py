from selenium import webdriver
from util.excel_util import ExcelUtil
import time
import unittest
import ddt
ex = ExcelUtil('D:\Kuban\config\waiterlogindata.xls')
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
        driver.find_element_by_xpath('//*[@id="sider"]/div/ul/li[5]/div').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="/locations/visitor$Menu"]/li[4]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="/locations/visitor/setting$Menu"]/li[3]/a').click()
        time.sleep(2)
        driver.find_element_by_id('visitor:name').send_keys(visitor_name)
        time.sleep(3)
        driver.find_element_by_id('visitor:email').send_keys(visitor_email)
        driver.find_element_by_id('visitor:phone_num').send_keys(visitor_phone)
        driver.find_element_by_id('visitor:company').send_keys(visitor_company)
        driver.find_element_by_id('notes').send_keys(visitor_notes)
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(3)
        try:
            driver.find_element_by_xpath('//*[@class="ant-modal-confirm-btns"]/button[2]').click()
        except:
            print('不需要审批哦')
        time.sleep(4)
        try:
            text = driver.find_element_by_class_name('ant-message').text
        except:
            text = '出错啦'
        print(text)

        #text2 = driver.find_element_by_class_name('ant-form-explain').text
        #print(text2)
        # if text == suc_msg:
        #     print('原来如此')
        # elif text2 == name_error:
        #     print('名字错啦')
        # elif text2 == email_error:
        #     print('邮箱错啦')
        # else:
        #     print('快看看咋回事')
        driver.close()
if __name__ == '__main__':
    unittest.main()