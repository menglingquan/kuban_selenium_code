from handle.admin_add_sapce_device_handle import AdminAddSpaceDeviceHandle
class AdminAddSpaceDeviceBusiness(object):
    def __init__(self,driver):
        self.asd = AdminAddSpaceDeviceHandle(driver)
    def admin_add_device(self):
        self.asd.click_device_menu()
        self.asd.click_device_addbtn()
        self.asd.send_device_name()
        self.asd.click_device_next()
        self.asd.send_device_option_name()
        self.asd.click_device_option_addbtn()
        self.asd.click_device_save()