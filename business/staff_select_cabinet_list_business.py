from handle.staff_select_cabinet_list_handle import StaffSelectCabinetListHandle
class StaffSelectCabinetListBusiness(object):
    def __init__(self,driver):
        self.sch = StaffSelectCabinetListHandle(driver)
    def staff_select_cabinet_list_base(self):
        self.sch.click_cabinet_menu()
        self.sch.click_cabinet_list()
        cabinet_error = self.sch.find_cabinet_page_error()
        if cabinet_error == None:
            return True
        return False