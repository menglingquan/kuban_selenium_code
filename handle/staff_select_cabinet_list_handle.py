from page.staff_select_cabinet_list_page import StaffSelectCabinetListPage
import time
class StaffSelectCabinetListHandle(object):
    def __init__(self,driver):
        self.scp = StaffSelectCabinetListPage(driver)
    def click_cabinet_menu(self):
        self.scp.get_cabinet_menu().click()
        time.sleep(1)
    def click_cabinet_list(self):
        self.scp.get_cabinet_list().click()
        time.sleep(1)
    def find_cabinet_page_error(self):
        try:
            cabinet_error = self.scp.get_cabinet_error().text
        except:
            cabinet_error = None
        return cabinet_error