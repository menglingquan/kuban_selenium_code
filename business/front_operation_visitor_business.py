from handle.front_operation_visitor_handle import FrontOperationVisitorHandle
class FrontOperationVisitorBusiness(object):
    def __int__(self,driver):
        self.fovh = FrontOperationVisitorHandle(driver)
    def frontoperationvisitor(self):
        self.fovh.click_visitor_menu()
        self.fovh.click_visitor_list()
        self.fovh.click_visitor()
        self.fovh.click_approval_button()
        self.fovh.click_approval_button()
        self.fovh.click_approval_confirm_button()
        self.fovh.click_back_list_button()
        self.fovh.click_first_sign_button()
        self.fovh.click_sign_confirm_button()
        self.fovh.click_select_all_list()
        self.fovh.click_sign_all_button()
        self.fovh.click_sign_out_button()
        self.fovh.click_select_all_list()
        self.fovh.click_sign_out_all_button()
        self.fovh.click_more_button()
        self.fovh.click_delect_button()
        self.fovh.click_delect_confirm_button()