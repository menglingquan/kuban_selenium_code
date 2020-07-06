from page.staff_invite_visitor_page import StaffInviteVisitorPage
class StaffInviteVisterHandle(object):
    def __init__(self,driver):
        self.ivp = StaffInviteVisitorPage(driver)
    def click_visitor_menu(self):
        self.ivp.get_visitor_menu().click()
    def click_visitor_list(self):
        self.ivp.get_visitor_list().click()
    def click_visitor_addbtn(self):
        self.ivp.get_visitor_addbtn().click()
    def send_visitor_name(self,visitor_name):
        self.ivp.get_visitor_name().send_keys(visitor_name)
    def send_visitor_email(self,visitor_email):
        self.ivp.get_visitor_email().send_keys(visitor_email)
    def send_visitor_phone(self,visitor_phone):
        self.ivp.get_visitor_phone().send_keys(visitor_phone)
    def send_visitor_company(self,visitor_company):
        self.ivp.get_visitor_company().send_keys(visitor_company)
    def send_visitor_notes(self,visitor_notes):
        self.ivp.get_visitor_notes().send_keys(visitor_notes)
    def submit_visitor(self):
        self.ivp.get_visitor_submit().click()
    def get_visitor_info_error_msg(self):
        try:
            infu_error_msg = self.ivp.get_visiter_info_error_msg().text
        except:
            infu_error_msg = None
        return infu_error_msg
    def get_suc_msg(self):
        try:
            suc_msg = self.ivp.get_visitor_suc().text
        except:
            suc_msg = None
        return suc_msg