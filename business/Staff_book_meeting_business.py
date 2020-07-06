from handle.staff_book_meeting_handle import StaffBookMeetingHandle
import time
class StaffBookMeetingBusiness(object):
    def __init__(self,driver):
        self.smh = StaffBookMeetingHandle(driver)
    def StaffBookMeetingBusiness_base(self,meeting_theme,meeting_issue):
        self.smh.click_meeting_modele()
        time.sleep(1)
        self.smh.click_book_room()
        time.sleep(1)
        self.smh.click_calendar()
        time.sleep(1)
        self.smh.send_meeting_theme_value(meeting_theme)
        self.smh.click_meeting_private()
        self.smh.send_meeting_issue_value(meeting_issue)
        self.smh.click_book_button()