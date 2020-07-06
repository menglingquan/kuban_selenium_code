from base.find_element import FindElement
class StaffBookMeetingPage(object):
    def __init__(self,driver):
        self.fe =FindElement(driver)
    def get_meeting_module(self):
        return self.fe.get_element('meeting_module')
    def get_book_room(self):
        return self.fe.get_element('book_room')
    def get_calendar(self):
        return self.fe.get_element('calendar')
    def get_meeting_theme(self):
        return self.fe.get_element('meeting_theme')
    def get_meeting_private(self):
        return self.fe.get_element('meeting_private')
    def get_meeting_issue(self):
        return self.fe.get_element('meeting_issue')
    def get_book_button(self):
        return self.fe.get_element('meeting_book_button')