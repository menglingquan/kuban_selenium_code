from base.find_element import FindElement
class StaffInviteListPage(object):
    def __init__(self,driver):
        self.fe = FindElement(driver)
    def get_visitor_menu(self):
        return self.fe.get_element('visitor_module')
    def get_visitor_list(self):
        return self.fe.get_element('visitor_list')
    def get_visitor_select_by_name(self):
        return self.fe.get_element('visitor_select_name_input')
    def get_visitor_list_first_name(self):
        return self.fe.get_element('visitor_list_first_name')
    def get_visitor_backlist(self):
        return self.fe.get_element('visitor_back_list')
    def get_visitor_list_export(self):
        return self.fe.get_element('visitor_list_export')
    def get_visitor_select_by_data(self):
        return self.fe.get_element('visitor_list_data_')
    def get_visitor_error_msg(self):
        return self.fe.get_element('visitor_error_msg')
