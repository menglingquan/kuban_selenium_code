from page.staff_book_list_page import StaffBookListPage
class StaffBookListHandle(object):
    def __init__(self,driver):
        self.slp = StaffBookListPage(driver)
    def click_meeting_modele(self):
        self.slp.get_meeting_module().click()
    def click_book_list(self):
        self.slp.get_book_list().click()
    def get_login_staff_name(self):
        login_name = self.slp.get_login_staff_name().text
        return login_name
    def get_list_staff_name(self):
        try:
            list_name = self.slp.get_list_staff_name().text
        except:
            list_name = None
        return list_name
    def click_list_staff_title(self):
        self.slp.get_list_meeting_title().click()
    def get_details_title(self):
        try:
            details_title=self.slp.get_details_staff_name().text
        except:
            details_title = None
        return details_title