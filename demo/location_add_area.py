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
try:
    driver.find_element_by_xpath('//button[@type="button"]').click()
    time.sleep(5)
except:
    print('yemeizhaodao')
driver.find_element_by_id('layer_description').send_keys('selenium楼层')
driver.find_element_by_class_name('ant-input-number-input').send_keys('1')
driver.find_element_by_xpath('//*[@class="ant-form ant-form-horizontal"]/div[4]/div/div/span/button').click()
time.sleep(1)
try:
    text1 = driver.find_element_by_class_name('ant-form-explain').text
    print(text1)
except:
    print('没毛病')
try:
    text4 = driver.find_element_by_class_name('ant-notification-notice-message').text

    print(text4)
except:
    print('没毛病')
time.sleep(5)
driver.find_element_by_xpath('//*[@id="/locations/desk$Menu"]/li[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@class="ant-table-tbody"]/tr/td').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@class="antd-pro-components-page-header-index-action"]/div/button[2]').click()

time.sleep(1)
driver.find_element_by_id('name').send_keys('123')
driver.find_element_by_xpath('//*[@id="area_type"]/div/div').click()
time.sleep(3)
try:
    driver.find_element_by_xpath('//*[@role="listbox"]/li').click()
    # driver.find_element_by_xpath('//*[@role="listbox"]/li[2]').click()
    # driver.find_element_by_xpath('//*[@role="listbox"]/li[3]').click()
    # driver.find_element_by_xpath('//*[@role="listbox"]/li[4]').click()
    print('棒')
except:
    print('buxing')
driver.find_element_by_id('size').send_keys('384')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="state"]/label/span/input').click()
driver.find_element_by_xpath('//*[@id="state"]/label[2]/span/input').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@class="ant-row"]/div/div[6]/div[2]/div/span/span/span/span').click()
time.sleep(1)
driver.find_element_by_class_name('ant-select-tree-title').click()
time.sleep(2)
driver.find_element_by_xpath('//button[@type="submit"]').click()
time.sleep(1)
try:
    text2 = driver.find_element_by_class_name('ant-form-explain').text
    print(text2)
except:
    print('没毛病')
try:
    text3 = driver.find_element_by_class_name('ant-notification-notice-message').text
    print(text3)
except:
    print('没毛病')
time.sleep(5)
driver.close()