from page.staff_book_meeting_page import StaffBookMeetingPage
class StaffBookMeetingHandle(object):
    def __init__(self,driver):
        self.smp = StaffBookMeetingPage(driver)
    def click_meeting_modele(self):
        self.smp.get_meeting_module().click()
    def click_book_room(self):
        self.smp.get_book_room().click()
    def click_calendar(self):
        self.smp.get_calendar().click()
    def send_meeting_theme_value(self,meeting_theme):
        self.smp.get_meeting_theme().send_keys(meeting_theme)
    def click_meeting_private(self):
        self.smp.get_meeting_private().click()
    def send_meeting_issue_value(self,meeting_issue):
        self.smp.get_meeting_issue().send_keys(meeting_issue)
    def click_book_button(self):
        self.smp.get_book_button().click()