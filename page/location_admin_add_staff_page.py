from base.find_element import FindElement
class LocationAdminAddStaffPage(object):
    def __init__(self,driver):
        self.fe = FindElement(driver)
    def find_staff_menu(self):
        return self.fe.get_element('location_staff_menu')
    def find_staff_add_btn(self):
        return self.fe.get_element('location_staff_add_button')
    def find_staff_name(self):
        return self.fe.get_element('men_name')
    def find_staff_job_number(self):
        return self.fe.get_element('user_id')
    def find_staff_space_title(self):
        return self.fe.get_element('space_title')
    def find_staff_phone_num(self):
        return self.fe.get_element('user_phone_num')
    def find_staff_email(self):
        return self.fe.get_element('user_email')
    def find_staff_add_submit(self):
        return self.fe.get_element('location_staff_add_submit')
    def find_staff_add_error_msg(self):
        return self.fe.get_element('tip_msg')
    def find_staff_from_tip_msg(self):
        return self.fe.get_element('staff_from_tip')
