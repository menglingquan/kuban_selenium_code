from base.find_element import FindElement
class LocationAdminAddFloorPage(object):
    def __int__(self,driver):
        self.fe = FindElement(driver)
    def get_desk_menu(self):
        return self.fe.get_element('')
    def get_desk_management(self):
        return self.fe.get_element('')
    def get_add_floor_btn(self):
        return self.fe.get_element('')
    def get_floor_name(self):
        return self.fe.get_element('')
    def get_floor_num(self):
        return self.fe.get_element('')
    def get_floor_note(self):
        return self.fe.get_element('')
    def get_add_floor_submit(self):
        return self.fe.get_element('')
    def get_form_tip(self):
        return self.fe.get_element('')
    def get_server_tip(self):
        return self.fe.get_element('')
