import time
from handle.staff_book_list_handle import StaffBookListHandle
class StaffBookListBusiness(object):
    def __init__(self,driver):
        self.slb = StaffBookListHandle(driver)
    def staff_book_list(self):
        self.slb.click_meeting_modele()
        time.sleep(3)
        self.slb.click_book_list()
        time.sleep(3)
        login_name = self.slb.get_login_staff_name()
        list_name = self.slb.get_list_staff_name()
        self.slb.click_list_staff_title()
        time.sleep(2)
        details_name = self.slb.get_details_title()
        time.sleep(2)
        if list_name == None:
            return True
        elif list_name == login_name and login_name == details_name and list_name ==login_name:
            return True
        return False