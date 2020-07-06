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
driver.find_element_by_xpath('//*[@id="sider"]/div/ul/li[5]/div').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="/locations/visitor$Menu"]/li[4]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="/locations/visitor/setting$Menu"]/li[9]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/button').click()
time.sleep(1)

driver.find_element_by_class_name('ant-form-item-children').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@role="listbox"]/li[1]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="blacklist_content"]').send_keys('好奇心')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div[1]/div/div/div[2]/div[2]/form/div[4]/div/div/span/button').click()
time.sleep(2)
driver.close()