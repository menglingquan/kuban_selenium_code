from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://mgmt.ent-dev.kuban.io/')
driver.find_element_by_id('phone_num').send_keys('14443543545')
time.sleep(2)
driver.find_element_by_id('login_sms_code').send_keys('123456')
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/form/div/div/div[2]/div[2]/div/div/span/button').click()
time.sleep(13)
driver.find_element_by_xpath('//*[@class="ant-layout-sider-children"]/ul/li[8]').click()
time.sleep(1)
try:
    driver.find_element_by_xpath('//*[@id="/locations/activity$Menu"]/li[2]').click()
    time.sleep(1)
except:
    print('meizhaodao')
driver.find_element_by_xpath('//button[@type="button"]').click()
time.sleep(1)
driver.find_element_by_id('title').send_keys('交友')
time.sleep(1)
driver.find_element_by_xpath('//*[@class="ant-modal-body"]/form/div[3]/div/div/span/button').click()
time.sleep(4)
driver.close()