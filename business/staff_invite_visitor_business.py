from handle.staff_invite_visitor_handle import StaffInviteVisterHandle
import time
class StaffInviteVisitorBusiness(object):
    def __init__(self,driver):
        self.ivh = StaffInviteVisterHandle(driver)
    def staff_invite_visitor_base(self,visitor_name,visitor_email,visitor_phone,visitor_company,visitor_notes,suc_msg,name_error,email_error):
        self.ivh.click_visitor_menu()
        time.sleep(1)
        self.ivh.click_visitor_list()
        time.sleep(1)
        self.ivh.click_visitor_addbtn()
        time.sleep(1)
        self.ivh.send_visitor_name(visitor_name)
        self.ivh.send_visitor_email(visitor_email)
        self.ivh.send_visitor_phone(visitor_phone)
        self.ivh.send_visitor_company(visitor_company)
        self.ivh.send_visitor_notes(visitor_notes)
        self.ivh.submit_visitor()
        time.sleep(3)
        visitor_info_error_msg = self.ivh.get_visitor_info_error_msg()
        suc_msg1 = self.ivh.get_suc_msg()

        if  suc_msg1 == suc_msg:
            return True
        elif visitor_info_error_msg == name_error:
            return True
        elif visitor_info_error_msg == email_error:
            return True
        return False
