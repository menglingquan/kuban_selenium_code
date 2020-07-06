from util.read_ini import ReadIni

class FindElement(object):
    def __init__(self,driver):
        self.driver = driver
    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            if by == 'name':
                return self.driver.find_element_by_name(value)
            if by == 'className':
                return self.driver.find_element_by_class_name(value)
            if by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            if by == 'linkText':
                return self.driver.find_element_by_link_text(value)
            if by == 'partialLinkText':
                return self.driver.find_element_by_partial_link_text(value)
        except:
            return None