from page.admin_add_space_devices_page import AdminAddSpaceDevicePage
class AdminAddSpaceDeviceHandle(object):
    def __init__(self,driver):
        self.asd = AdminAddSpaceDevicePage(driver)
    def click_device_menu(self):
        return self.asd.get_device_menu().click()
    def click_device_addbtn(self):
        return self.asd.get_device_addbtn().click()
    def send_device_name(self,device_name):
        return self.asd.get_device_name().send_keys(device_name)
    def click_device_next(self):
        return self.asd.get_device_next().click()
    def send_device_option_name(self,option_name):
        return self.asd.get_device_option_name().send_keys(option_name)
    def click_device_option_addbtn(self):
        return self.asd.get_device_option_addbtn().click()
    def click_device_save(self):
        return self.asd.get_device_save().click()
    def get_page_tip_text(self):
        try:
            page_tip = self.asd.get_page_tip().text
        except:
            page_tip = None
        return page_tip
    def get_sever_tip_next(self):
        try:
            server_tip = self.asd.get_server_tip().text
        except:
            server_tip = None
        return server_tip