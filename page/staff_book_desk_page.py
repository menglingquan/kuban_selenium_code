from base.find_element import FindElement
class StaffBookDeskPage(object):
    def __init__(self,driver):
        self.fe = FindElement(driver)
    def get_desk_module(self):
        return self.fe.get_element('desk_model')
    def get_desk_list(self):
        return self.fe.get_element('desk_list')
    def get_desk(self):
        return self.fe.get_element('desk_choose')
    def get_desk_submit(self):
        return self.fe.get_element('desk_book')
    def get_desk_submit_again(self):
        return self.fe.get_element('desk_again')
    def get_desk_book_suc_msg(self):
        return self.fe.get_element('desk_suc')