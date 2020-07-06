from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get('https://mgmt.ent.kuban.io/user/login')
try:
    driver.find_element_by_id('phone_num').send_keys('16724453466')
except:
    print('咋回事啊')

time.sleep(6)
driver.close()