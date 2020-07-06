from handle.add_address_book_handle import AddAddressHandle
class AddAddressBookBusiness(object):
    def __init__(self,driver):
        self.aah = AddAddressHandle(driver)
    def add_address_book_base(self,user_name,user_company,user_phone,user_email,user_notes):
        self.aah.click_mine()
        self.aah.click_address_book()
        self.aah.click_address_book_addbtn()
        self.aah.send_user_name(user_name)
        self.aah.send_user_company(user_company)
        self.aah.send_user_phone(user_phone)
        self.aah.send_user_email(user_email)
        self.aah.send_user_notes(user_notes)
        self.aah.click_address_boon_submit()