from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://mgmt.ent-dev.kuban.io/')
driver.find_element_by_id('phone_num').send_keys('14443543545')
time.sleep(2)
driver.find_element_by_id('login_sms_code').send_keys('123456')
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/form/div/div/div[2]/div[2]/div/div/span/button').click()
time.sleep(13)
driver.find_element_by_xpath('//*[@class="ant-layout-sider-children"]/ul/li[3]').click()
time.sleep(1)
try:
    driver.find_element_by_xpath('//*[@id="/locations/desk$Menu"]/li[1]').click()
    time.sleep(1)
except:
    print('meizhaodao')

driver.find_element_by_xpath('//*[@class="ant-table-tbody"]/tr/td').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@class="ant-table-tbody"]/tr').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@class="ant-card-extra"]/div/button').click()
time.sleep(1)
driver.find_element_by_id('preDesk').send_keys('11')
driver.find_element_by_id('initDesk').send_keys('3')
driver.find_element_by_id('numDesk').send_keys('3')
driver.find_element_by_xpath('//button[@type="submit"]').click()
time.sleep(3)
driver.close()