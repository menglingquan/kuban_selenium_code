from handle.add_menberhandle import AddMenHandle
import time
class AddMenBusiness(object):
    def __init__(self,driver):
        self.amh = AddMenHandle(driver)
    def login_base(self,menName,menID,sapceTitle,menPhone,menEmail):
        self.amh.click_men_list()
        time.sleep(1)
        self.amh.click_men_add_btn()
        time.sleep(1)
        self.amh.send_men_name(menName)
        time.sleep(1)
        self.amh.send_men_id(menID)
        self.amh.send_men_sapce_title(sapceTitle)
        time.sleep(3)
        self.amh.send_men_phone_num(menPhone)
        time.sleep(3)
        self.amh.send_men_email(menEmail)
        self.amh.click_men_insert_btn()
        time.sleep(3)


    def add_men_function(self,menName,menID,spaceTitle,menPhone,menEmail):
        self.login_base(menName,menID,spaceTitle,menPhone,menEmail)
        # if self.amh.get_men_add_suc_msg(MenAddSuc, assertText) == None:
        #     print(',MenAddSuc,assertText')
        #     return True
        # else:
        #     print('')
        #     return False