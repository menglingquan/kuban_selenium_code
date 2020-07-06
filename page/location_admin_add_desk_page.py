from base.find_element import FindElement
class LocationAdminAddDeskPage(object):
    def __int__(self,driver):
        self.fe = FindElement(driver)
    def get_desk_menu(self):
        return self.fe.get_element('')
    def get_desk_management(self):
        return self.fe.get_element('')
    def get_first_floor(self):
        return self.fe.get_element('')
    def get_first_area(self):
        return self.fe.get_element('')
    def get_add_desk_btn(self):
        return self.fe.get_element('')
    def get_desk_prefix(self):
        return self.fe.get_element('')
    def get_desk_start_num(self):
        return self.fe.get_element('')
    def get_desk_num(self):
        return self.fe.get_element('')
    def get_add_desk_submit(self):
        return self.fe.get_element('')
    def get_form_tip(self):
        return self.fe.get_element('')
    def get_server_tip(self):
        return self.fe.get_element('')