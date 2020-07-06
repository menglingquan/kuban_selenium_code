from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://mgmt.ent-dev.kuban.io/')
driver.find_element_by_id('phone_num').send_keys('18293988402')
time.sleep(2)
driver.find_element_by_id('login_sms_code').send_keys('123456')
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/form/div/div/div[2]/div[2]/div/div/span/button').click()
time.sleep(16)
driver.find_element_by_xpath('//*[@id="sider"]/div/ul/li[3]/div').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="/locations/meeting$Menu"]/li[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="/locations/meeting$Menu"]/li[2]').click()
time.sleep(3)
nsmr = driver.find_element_by_class_name('antd-pro-components-global-header-index-name').text
print(nsmr)
time.sleep(3)
name = driver.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div[2]/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/div/div/div[1]/h4').text
name1 = driver.find_element_by_xpath('//*[@class="ant-table-tbody"]/tr/td/div/div/div/h4').text
print(name)
print(name1)
time.sleep(3)
if nsmr == name:
    print('gfdggsfd')
driver.find_element_by_class_name('antd-pro-components-ellipsis-index-ellipsis').click()
time.sleep(5)
driver.close()