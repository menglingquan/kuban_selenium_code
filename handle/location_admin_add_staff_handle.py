from page.location_admin_add_staff_page import LocationAdminAddStaffPage
import time
class LocationAdminAddStaffHandle(object):
    def __init__(self,driver):
        self.lap = LocationAdminAddStaffPage(driver)
    def click_staff_menu(self):
        self.lap.find_staff_menu().click()
        time.sleep(1)
    def click_staff_add_btn(self):
        self.lap.find_staff_add_btn().click()
        time.sleep(1)
    def send_staff_name(self,staff_name):
        self.lap.find_staff_name().send_keys(staff_name)
        time.sleep(0.5)
    def send_staff_job_number(self,staff_job_number):
        self.lap.find_staff_job_number().send_keys(staff_job_number)
        time.sleep(0.5)
    def send_staff_space_title(self,staff_space_title):
        self.lap.find_staff_space_title().send_keys(staff_space_title)
        time.sleep(0.5)
    def send_staff_phone_num(self,staff_phone_num):
        self.lap.find_staff_phone_num().send_keys(staff_phone_num)
        time.sleep(0.5)
    def send_staff_email(self,staff_email):
        self.lap.find_staff_email().send_keys(staff_email)
        time.sleep(0.5)
    def click_staff_add_submit(self):
        self.lap.find_staff_add_submit().click()
        time.sleep(1)
    def get_staff_add_error_msg(self):
        try:
            tip_msg = self.lap.find_staff_add_error_msg().text
            time.sleep(0.5)
        except:
            tip_msg = None
        return tip_msg
    def get_staff_from_tip_msg(self):
        try:
            form_tip_msg = self.lap.find_staff_from_tip_msg().text
        except:
            form_tip_msg = None
        return form_tip_msg