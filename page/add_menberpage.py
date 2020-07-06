from base.find_element import FindElement
class AddMenPage(object):
    def __init__(self,driver):
        self.fe = FindElement(driver)
    def get_men_list_element(self):
        return self.fe.get_element('men_list')
    def get_men_add_btn_element(self):
        return self.fe.get_element('men_add_btn')
    def get_men_name_element(self):
        return self.fe.get_element('men_name')
    def get_men_id_element(self):
        return self.fe.get_element('job_number')
    def get_men_space_title_element(self):
        return self.fe.get_element('space_title')
    def get_men_phone_num_element(self):
        return self.fe.get_element('user_phone_num')
    def get_men_emai_element(self):
        return self.fe.get_element('user_email')
    def get_men_insert_btn_element(self):
        return self.fe.get_element('user_add_btn')
    def get_men_add_success_msg(self):
        return self.fe.get_element('user_add_success_message')
