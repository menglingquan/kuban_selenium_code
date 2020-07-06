from base.find_element import FindElement
class StaffSelectCabinetListPage(object):
    def __init__(self,driver):
        self.fe = FindElement(driver)
    def get_cabinet_menu(self):
        return self.fe.get_element('cabinet_menu')
    def get_cabinet_list(self):
        return self.fe.get_element('cabinet_list')
    def get_cabinet_error(self):
        return self.fe.get_element('cabinet_list_error')
