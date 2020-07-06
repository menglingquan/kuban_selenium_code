from page.staff_book_desk_page import StaffBookDeskPage
class StaffBookDeskHandle(object):
    def __init__(self,driver):
        self.sdp = StaffBookDeskPage(driver)
    def click_desk_module(self):
        self.sdp.get_desk_module().click()
    def click_desk_list(self):
        self.sdp.get_desk_list().click()
    def click_desk(self):
        self.sdp.get_desk().click()
    def click_desk_submit(self):
        self.sdp.get_desk_submit().click()
    def click_desk_submit_again(self):
        self.sdp.get_desk_submit_again().click()
    def get_desk_book_suc_msg(self):
        try:
            suc_msg = self.sdp.get_desk_book_suc_msg().text
            suc_msg_judge = suc_msg[-4:]
        except:
            suc_msg_judge = None
        return suc_msg_judge