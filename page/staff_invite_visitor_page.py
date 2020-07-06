from base.find_element import FindElement
class StaffInviteVisitorPage(object):
    def __init__(self,driver):
        self.fe = FindElement(driver)
    def get_visitor_menu(self):
        return self.fe.get_element('visitor_module')
    def get_visitor_list(self):
        return self.fe.get_element('visitor_list')
    def get_visitor_addbtn(self):
        return self.fe.get_element('visitor_addbtn')
    def get_visitor_name(self):
        return self.fe.get_element('visitor_name')
    def get_visitor_email(self):
        return self.fe.get_element('visitor_email')
    def get_visitor_phone(self):
        return self.fe.get_element('visitor_phone')
    def get_visitor_company(self):
        return self.fe.get_element('visitor_company')
    def get_visitor_notes(self):
        return self.fe.get_element('visitor_notes')
    def get_visitor_submit(self):
        return self.fe.get_element('visitor_submit')
    def get_visiter_info_error_msg(self):
        return self.fe.get_element('visitor_info_error')
    def get_visitor_suc(self):
        return self.fe.get_element('visitor_suc')