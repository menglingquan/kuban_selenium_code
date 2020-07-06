from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://mgmt.ent-dev.kuban.io/')
driver.find_element_by_id('phone_num').send_keys('18293988402')
time.sleep(2)
driver.find_element_by_id('login_sms_code').send_keys('123456')
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/form/div/div/div[2]/div[2]/div/div/span/button').click()
time.sleep(16)
driver.find_element_by_xpath('//*[@id="sider"]/div/ul/li[5]/div').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="/locations/cabinet$Menu"]/li[1]').click()
time.sleep(1)
try:
    error = driver.find_element_by_class_name('ant-notification-notice-message').text
    print(error)
except:
    print('一切正常。over')
driver.close()