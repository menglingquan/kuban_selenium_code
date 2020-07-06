from page.frontwaiter_invite_visitor_page import FronWaiterInviteVisitorPage
import time
class FrontWaiterInviteVisterHandle(object):
    def __init__(self,driver):
        self.fivp = FronWaiterInviteVisitorPage(driver)
    def click_visitor_menu(self):
        self.fivp.get_visitor_menu().click()
        time.sleep(1)
    def click_visitor_list(self):
        self.fivp.get_visitor_list().click()
        time.sleep(1)
    def click_sign_addbtn(self):
        self.fivp.get_sign_addbtn().click()
        time.sleep(1)
    def send_visitor_name(self,visitor_name):
        self.fivp.get_visitor_name().send_keys(visitor_name)
    def send_visitor_email(self,visitor_email):
        self.fivp.get_visitor_email().send_keys(visitor_email)
    def send_visitor_phone(self,visitor_phone):
        self.fivp.get_visitor_phone().send_keys(visitor_phone)
    def send_visitor_company(self,visitor_company):
        self.fivp.get_visitor_company().send_keys(visitor_company)
    def send_visitor_notes(self,visitor_notes):
        self.fivp.get_visitor_notes().send_keys(visitor_notes)
    def submit_visitor(self):
        self.fivp.get_visitor_submit().click()
        time.sleep(3)
    def get_visitor_info_error_msg(self):
        try:
            infu_error_msg = self.fivp.get_visiter_info_error_msg().text
        except:
            infu_error_msg = None
        return infu_error_msg
    def click_visitor_approval(self):
        try:
            self.fivp.get_visitor_approval().click()
            time.sleep(3)
        except:
            pass
    def get_suc_msg(self):
        try:
            suc_msg = self.fivp.get_visitor_suc().text
        except:
            suc_msg = None
        return suc_msg