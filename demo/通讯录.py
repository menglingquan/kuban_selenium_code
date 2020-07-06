from selenium import webdriver
from util.excel_util import ExcelUtil
import time
import unittest
import ddt
driver = webdriver.Chrome()
driver.get('https://mgmt.ent-dev.kuban.io/')
driver.find_element_by_id('phone_num').send_keys('17600909177')
time.sleep(2)
driver.find_element_by_id('login_sms_code').send_keys('123456')
driver.find_element_by_xpath(
    '//*[@id="root"]/div/div/div/form/div/div/div[2]/div[2]/div/div/span/button').click()
time.sleep(16)
driver.find_element_by_class_name('antd-pro-components-global-header-index-name').click()
time.sleep(0.2)
driver.find_element_by_xpath('//*[@role="menu"]/li/i').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@type="button"]').click()
time.sleep(2)
driver.find_element_by_id('name').send_keys('123')
time.sleep(1)
driver.find_element_by_id('company').send_keys('公司')
driver.find_element_by_id('phone_num').send_keys('18845647700')
driver.find_element_by_id('email').send_keys('188237637.com')
driver.find_element_by_id('notes').send_keys('备注啦')


driver.find_element_by_xpath('//*[@type="submit"]').click()
time.sleep(0.5)
try:
    page_tip = driver.find_element_by_class_name('ant-form-explain').text
    a = page_tip[0,3]
    if a == '请输入':
        print('niuB')
except:
    print('页面没有错误0')
time.sleep(2)
driver.close()