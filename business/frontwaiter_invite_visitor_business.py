from handle.frontwaiter_invite_visitor_handle import FrontWaiterInviteVisterHandle
class FrontWaiterInviteVisitorBusiness(object):
    def __init__(self,driver):
        self.fivh = FrontWaiterInviteVisterHandle(driver)
    def fronwaiterinvitevisitor(self,visitor_name,visitor_email,visitor_phone,visitor_company,visitor_notes,suc_msg,name_error,email_error):
        self.fivh.click_visitor_menu()
        self.fivh.click_visitor_list()
        self.fivh.click_sign_addbtn()
        self.fivh.send_visitor_name(visitor_name)
        self.fivh.send_visitor_email(visitor_email)
        self.fivh.send_visitor_phone(visitor_phone)
        self.fivh.send_visitor_company(visitor_company)
        self.fivh.send_visitor_notes(visitor_notes)
        self.fivh.submit_visitor()
        visitor_info_error_msg = self.fivh.get_visitor_info_error_msg()
        self.fivh.click_visitor_approval()
        suc_msg1 = self.fivh.get_suc_msg()
        if  suc_msg1 == suc_msg:
            return True
        elif visitor_info_error_msg == name_error:
            return True
        elif visitor_info_error_msg == email_error:
            return True
        return False