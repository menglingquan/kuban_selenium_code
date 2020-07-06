from page.front_operation_visitor_page import FrontOperationVisitorPage
import time
class FrontOperationVisitorHandle(object):
    def __init__(self,driver):
        self.fovp = FrontOperationVisitorPage(driver)
    def click_visitor_menu(self):
        self.fovp.get_visitor_menu().click()
    def click_visitor_list(self):
        self.fovp.get_visitor_list().click()
    def click_visitor(self):
        self.fovp.get_visitor_info().click()
    def click_approval_button(self):
        self.fovp.get_approval_button().click()
    def click_approval_confirm_button(self):
        self.fovp.get_approval_confirm_button().click()
    def click_back_list_button(self):
        self.fovp.get_back_list_button().click()
    def click_select_all_list(self):
        self.fovp.get_select_all_list().click()
    def click_approval_all_button(self):
        self.fovp.get_approval_all_button().click()
    def click_first_sign_button(self):
        self.fovp.get_first_sign_button().click()
    def click_sign_all_button(self):
        self.fovp.get_sign_all_button().click()
    def click_sign_confirm_button(self):
        self.fovp.get_sign_confirm_button().click()
    def click_sign_out_button(self):
        self.fovp.get_sign_out_button().click()
    def click_sign_out_all_button(self):
        self.fovp.get_sign_out_all_button().click()
    def click_more_button(self):
        self.fovp.get_more_button().click()
    def click_delect_button(self):
        self.fovp.get_delect_button()
    def click_delect_confirm_button(self):
        self.fovp.get_delect_confirm_button()