from base.find_element import FindElement
class LocationAdminAddDRoomPage(object):
    def __int__(self,driver):
        self.fe = FindElement(driver)
    def get_room_menu(self):
        return self.fe.get_element('')
    def get_room_management(self):
        return self.fe.get_element('')
    def get_room_add_btn(self):
        return self.fe.get_element('')
    def get_room_name(self):
        return self.fe.get_element('')
    def get_room_type(self):
        return self.fe.get_element('')
    def get_room_floor(self):
        return self.fe.get_element('')
    def get_room_maxpeople(self):
        return self.fe.get_element('')
    def get_room_size(self):
        return self.fe.get_element('')
    def get_add_room_submit(self):
        return self.fe.get_element('')
    def get_form_tip(self):
        return self.fe.get_element('')
    def get_server_tip(self):
        return self.fe.get_element('')