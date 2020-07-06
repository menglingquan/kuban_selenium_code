from handle.staff_book_desk_handle import StaffBookDeskHandle
import time
class StaffBookDeskBusiness(object):
    def __init__(self,driver):
        self.sdh = StaffBookDeskHandle(driver)
    def staff_book_desk(self):
        self.sdh.click_desk_module()
        time.sleep(1)
        self.sdh.click_desk_list()
        time.sleep(1)
        self.sdh.click_desk()
        time.sleep(1)
        self.sdh.click_desk_submit()
        time.sleep(2)
        self.sdh.click_desk_submit_again()
        time.sleep(2)
        suc_msg = self.sdh.get_desk_book_suc_msg()
        if suc_msg == '预定成功':
            return True
        elif suc_msg == '已被预定':
            return True
        elif suc_msg == '配的部门':
            return True
        return False