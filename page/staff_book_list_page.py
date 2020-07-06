from base.find_element import FindElement
class StaffBookListPage(object):
    def __init__(self,driver):
        self.fe = FindElement(driver)
    def get_meeting_module(self):
        return self.fe.get_element('meeting_module')
    def get_book_list(self):
        return self.fe.get_element('book_list')
    def get_login_staff_name(self):
        return self.fe.get_element('login_staff_name')
    def get_list_staff_name(self):
        return self.fe.get_element('list_staff_name')
    def get_list_meeting_title(self):
        return self.fe.get_element('list_meeting_title')
    def get_details_staff_name(self):
        return self.fe.get_element('details_staff_name')