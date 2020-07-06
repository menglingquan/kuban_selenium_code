from page.location_admin_add_activity_page import LocationAdminAddActivityPage
import time
class LoactionAdminAddActivityHandle(object):
    def __init__(self,driver):
        self.laa = LocationAdminAddActivityPage(driver)
    def click_activity_menu(self):
        self.laa.get_activity_menu().click()
        time.sleep(1)
    def click_activity_management(self):
        self.laa.get_activity_management().click()
        time.sleep(1)
    def click_activity_add_btn(self):
        self.laa.get_activity_add_btn().click()
        time.sleep(1)
    def send_activity_title(self, activity_title):
        self.laa.get_activity_title().send_keys(activity_title)
    def click_activity_type_input(self):
        self.laa.get_activity_type_input().click()
        time.sleep(1)
    def click_activity_type(self):
        self.laa.get_activity_type().click()
        time.sleep(1)
    def click_activity_time_input(self):
        self.laa.get_activity_time_input().click()
        time.sleep(1)
    def click_activity_start_time(self):
        self.laa.get_activity_start_time().click()
        time.sleep(1)
    def click_activity_end_time(self):
        self.laa.get_activity_end_time().click()
        time.sleep(1)
    def click_activity_time_confirm(self):
        self.laa.get_activity_time_confirm().click()
        time.sleep(1)
    def click_activity_singup_by_end_input(self):
        self.laa.get_activity_singup_by_end_input().click()
        time.sleep(1)
    def click_activity_signup_by_end_next_month(self):
        self.laa.get_activity_signup_by_end_next_month().click()
    def click_activity_singup_by_end_time(self):
        self.laa.get_activity_singup_by_end_time().click()
        time.sleep(1)
    def send_activity_space(self,activity_space):
        self.laa.get_activity_space().send_keys(activity_space)
    def send_activity_tickets(self,activity_ticket):
        self.laa.get_activity_tickets().send_keys(activity_ticket)
    def click_acrivity_notop(self):
        self.laa.get_activity_notop().click()
        time.sleep(1)
    def click_activity_top(self):
        self.laa.get_activity_top().click()
        time.sleep(1)
    def send_activity_uploadpic(self,pic_path):
        self.laa.get_activity_uploadpic().send_keys(pic_path)
        time.sleep(3)
    def send_activity_note(self,activity_note):
        self.laa.get_activity_note().send_keys(activity_note)
    def click_activity_add_release(self):
        self.laa.get_activity_add_release().click()
        time.sleep(3)
    def click_activity_add_draff(self):
        self.laa.get_activity_add_draft().click()