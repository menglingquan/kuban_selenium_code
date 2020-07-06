from selenium import webdriver
import time
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
driver.find_element_by_xpath('//*[@id="/locations/visitor/setting$Menu"]/li[3]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@class="antd-pro-layouts-page-header-layout-content"]/div/div/div/div/div/button').click()
time.sleep(2)
driver.find_element_by_class_name('ant-input').send_keys('勇闯天涯3')
time.sleep(2)
driver.find_element_by_xpath('//*[@type="button"]').click()
print('1111111')
time.sleep(4)
driver.find_element_by_xpath('//*[@id="root"]/div/section/section/main/div/div[2]/div/div[1]/div[2]/button').click()
print('123412')
time.sleep(2)
time.sleep(1)
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