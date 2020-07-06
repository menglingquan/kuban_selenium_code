from handle.location_admin_add_staff_handle import LocationAdminAddStaffHandle
class LocationAdminAddStaffBusiness(object):
    def __init__(self,driver):
        self.lah = LocationAdminAddStaffHandle(driver)
    def location_admin_add_staff(self,staff_name,staff_job_number,staff_space_title,staff_phone_num,staff_email):
        self.lah.click_staff_menu()
        self.lah.click_staff_add_btn()
        self.lah.send_staff_name(staff_name)
        self.lah.send_staff_job_number(staff_job_number)
        self.lah.send_staff_space_title(staff_space_title)
        self.lah.send_staff_phone_num(staff_phone_num)
        self.lah.send_staff_email(staff_email)
        self.lah.click_staff_add_submit()
        msg = self.lah.get_staff_add_error_msg()
        if msg == '':
            return True
        elif msg == '':
            return False
        else:
            return False
        form_msg = self.lah.get_staff_from_tip_msg()
        if form_msg == None:
            return True
        elif form_msg == '请填写员工姓名':
            return True