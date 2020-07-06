from page.add_address_book_page import AddAddressPage
class AddAddressHandle(object):
    def __init__(self,driver):
        self.aap = AddAddressPage(driver)
    def click_mine(self):
        self.aap.find_mine().click()
    def click_address_book(self):
        self.aap.find_address().click()
    def click_address_book_addbtn(self):
        self.aap.find_address_addbtn().click()
    def send_user_name(self,user_name):
        self.aap.find_user_name().send_keys(user_name)
    def send_user_company(self,user_company):
        self.aap.find_user_compony().send_keys(user_company)
    def send_user_phone(self,user_phone):
        self.aap.find_user_phone().send_keys(user_phone)
    def send_user_email(self,user_email):
        self.aap.find_user_email().send_keys(user_email)
    def send_user_notes(self,user_notes):
        self.aap.find_user_notes().send_keys(user_notes)
    def click_address_boon_submit(self):
        self.aap.find_address_submit().click()
    def get_page_tip(self):
        try:
            page_tip = self.aap.find_page_tip().text
        except:
            page_tip = None
        return page_tip
    def get_server_tip(self):
        try:
            server_tip = self.aap.find_server_tip().text
        except:
            server_tip = None
        return server_tip
