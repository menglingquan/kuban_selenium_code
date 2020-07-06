from handle.staff_invite_visitor_plist_handle import StaffInviteListHandle
import time
class StaffInviteListBusiness(object):
    def __init__(self,driver):
        self.ilh = StaffInviteListHandle(driver)
    def staff_invite_list_base(self,visitor_name,visitor_email,visitor_phone,visitor_company,visitor_notes,suc_msg,name_error,email_error):
        self.ilh.click_visitor_menu()
        time.sleep(1)
        self.ilh.click_visitor_list()
        time.sleep(1)
        self.ilh.input_select_by_name(visitor_name)
        time.sleep(1)
        self.ilh.get_list_first_name_msg()
        self.ilh.click_list_first_name()
        time.sleep(1)
        self.ilh.get_visitor_info_msg()
        self.ilh.click_visitor_infu_backlist()
        time.sleep(1)
        self.ilh.click_visitor_export()
        time.sleep(1)
        self.ilh.get_visitor_error_msg()