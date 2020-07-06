from base.find_element import FindElement
class AddAddressPage(object):
    def __init__(self,driver):
        self.fe = FindElement(driver)
    def find_mine(self):
        return self.fe.get_element('')
    def find_address(self):
        return self.fe.get_element('')
    def find_address_addbtn(self):
        return self.fe.get_element('')
    def find_user_name(self):
        return self.fe.get_element('')
    def find_user_compony(self):
        return self.fe.get_element('')
    def find_user_phone(self):
        return self.fe.get_element('')
    def find_user_email(self):
        return self.fe.get_element('')
    def find_user_notes(self):
        return self.fe.get_element('')
    def find_address_submit(self):
        return self.fe.get_element('')
    def find_page_tip(self):
        return self.fe.get_element('')
    def find_server_tip(self):
        return self.fe.get_element('')
