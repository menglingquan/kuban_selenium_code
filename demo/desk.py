from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://mgmt.ent-dev.kuban.io/')
driver.find_element_by_id('phone_num').send_keys('18293988402')
time.sleep(2)
driver.find_element_by_id('login_sms_code').send_keys('123456')
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/form/div/div/div[2]/div[2]/div/div/span/button').click()
time.sleep(16)
driver.find_element_by_xpath('//*[@id="sider"]/div/ul/li[2]/div').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="/locations/desk$Menu"]/li[1]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@class="antd-pro-pages-desk-components-desk-icon-deskAvatar"]/div').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@class="drawer-footer"]/button').click()

time.sleep(3)
try:
    a = driver.find_element_by_xpath('//*[@class="drawer-footer"][2]/button')
    b=a.text
    print(b)
    time.sleep(2)
    a.click()
    time.sleep(2)
except:
    print('无法点击')

try:
    text = driver.find_element_by_class_name('ant-notification-notice-message').text
except:
    text = None
    print('没定位到哇')
print(text)
print('牛B')
driver.close()