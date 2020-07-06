from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://mgmt.ent-dev.kuban.io/')
driver.find_element_by_id('phone_num').send_keys('14443543545')
time.sleep(2)
driver.find_element_by_id('login_sms_code').send_keys('123456')
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/form/div/div/div[2]/div[2]/div/div/span/button').click()
time.sleep(13)
driver.find_element_by_xpath('//*[@class="ant-layout-sider-children"]/ul/li[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@class="antd-pro-pages-location-member-location-members-memberBtns"]/button[3]').click()
time.sleep(2)
driver.find_element_by_id('name').send_keys('测试员工')
time.sleep(2)
driver.find_element_by_id('job_number').send_keys('0001')
time.sleep(2)
driver.find_element_by_id('space_title').send_keys('测试')
time.sleep(2)
driver.find_element_by_id('phone_num').send_keys('19747385758')
time.sleep(2)
driver.find_element_by_id('email').send_keys('19747385758@qq.com')
time.sleep(2)
driver.find_element_by_xpath('//button[@type="button"]').click()
try:
    get_msg = driver.find_element_by_class_name('ant-notification-notice-message').text
    print(get_msg)
except:
    get_msg = None
if get_msg == '抱歉，页面出错了':
    print('网络错误')
elif get_msg == '服务器发生错误':
    print('服务器错误')
else:
    print('没毛病')
time.sleep(12)
driver.close()
