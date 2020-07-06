from page.add_menberpage import AddMenPage
from page.loginpage import LoginPage
class AddMenHandle(object):
    def __init__(self,driver):
        self.amp = AddMenPage(driver)
        self.lp = LoginPage(driver)
    def click_men_list(self):
        self.amp.get_men_list_element().click()
    def click_men_add_btn(self,):
        self.amp.get_men_add_btn_element().click()
    def send_men_name(self,menName):
        self.amp.get_men_name_element().send_keys(menName)
    def send_men_id(self,id):
        self.amp.get_men_id_element().send_keys(id)
    def send_men_sapce_title(self,spaceTitle):
        self.amp.get_men_space_title_element().send_keys(spaceTitle)
    def send_men_phone_num(self,menPhone):
        self.amp.get_men_phone_num_element().send_keys(menPhone)
    def send_men_email(self,menEmail):
        self.amp.get_men_phone_num_element().send_keys(menEmail)
    def click_men_insert_btn(self):
        self.amp.get_men_phone_num_element().click()

    def get_men_add_suc_msg(self,info,msg_info):
        try:
            if info == 'user_add_success_message':
                text = self.amp.get_men_add_success_msg().text
        except:
            text = None
        return text