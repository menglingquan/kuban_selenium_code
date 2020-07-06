from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://mgmt.ent-dev.kuban.io/')
driver.find_element_by_id('phone_num').send_keys('14443543545')
time.sleep(2)
driver.find_element_by_id('login_sms_code').send_keys('123456')
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/form/div/div/div[2]/div[2]/div/div/span/button').click()
time.sleep(13)
driver.find_element_by_class_name('antd-pro-components-global-header-index-name').click()
time.sleep(4)
try:
    driver.find_element_by_class_name('ant-dropdown-menu-item').click()
except:
    print('hahah')
time.sleep(1)
driver.find_element_by_xpath('//button[@type="button"]').click()

time.sleep(2)
driver.find_element_by_id('name').send_keys('123')
driver.find_element_by_id('company').send_keys('234')
driver.find_element_by_id('phone_num').send_keys('18845647733')
driver.find_element_by_id('email').send_keys('188456422@qq.com')
driver.find_element_by_xpath('//button[@type="submit"]').click()

time.sleep(3)
driver.close()