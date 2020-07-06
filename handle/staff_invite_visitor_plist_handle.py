from page.staff_invite_visitor_plist_page import StaffInviteListPage
class StaffInviteListHandle(object):
    def __init__(self,driver):
        self.ilp = StaffInviteListPage(driver)
    def click_visitor_menu(self):
        self.ilp.get_visitor_menu().click()
    def click_visitor_list(self):
        self.ilp.get_visitor_list().click()
    def input_select_by_name(self,visitor_name):
        self.ilp.get_visitor_select_by_name().send_keys(visitor_name)
    def get_list_first_name_msg(self):
        try:
            first_name = self.ilp.get_visitor_list_first_name().text
        except:
            first_name = None
        return first_name
    def click_list_first_name(self):
        self.ilp.get_visitor_list_first_name().click()
    def get_visitor_info_msg(self):
        try:
            visitor_info = self.ilp.get_visitor_backlist().text
        except:
            visitor_info = None
        return visitor_info
    def click_visitor_infu_backlist(self):
        self.ilp.get_visitor_backlist().click()
    def click_visitor_export(self):
        self.ilp.get_visitor_list_export().click()
    def click_visitor_select_by_data(self):
        self.ilp.get_visitor_select_by_data().click()
    def get_visitor_error_msg(self):
        try:
            error_msg = self.ilp.get_visitor_error_msg().text
        except:
            error_msg = None
        return error_msg