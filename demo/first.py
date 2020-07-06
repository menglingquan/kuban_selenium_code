import time
import random
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

def driver_init():
    driver.get('https://www.baidu.com')
    time.sleep(5)
def get_element(id):
    driver.implicity_wait(10)
    element = driver.find_element_by_id(id)
    return element
def get_element_by_classname(calssName):
    element = driver.find_element_by_class_name(calssName)
    return element
def get_range_val():
    num = ''.join(random.sample('123456789abcefghijklmnopq',3))
    return num

if __name__ == '__main__':
    values ='123123'
    driver_init()
    get_element('kk').send_keys(values)
    te = get_element('su').text
    print(te)
    time.sleep(3)
    driver.close()


