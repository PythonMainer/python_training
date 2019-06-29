

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        dw = self.app.dw
        # open create page contact
        dw.find_element_by_link_text("add new").click()
        # fill contact form
        dw.find_element_by_name("firstname").click()
        dw.find_element_by_name("firstname").clear()
        dw.find_element_by_name("firstname").send_keys(contact.firstname)
        dw.find_element_by_name("middlename").clear()
        dw.find_element_by_name("middlename").send_keys(contact.middlename)
        dw.find_element_by_name("lastname").clear()
        dw.find_element_by_name("lastname").send_keys(contact.lastname)
        dw.find_element_by_name("nickname").click()
        dw.find_element_by_name("nickname").clear()
        dw.find_element_by_name("nickname").send_keys(contact.nickname)
        dw.find_element_by_name("address").click()
        dw.find_element_by_name("address").clear()
        dw.find_element_by_name("address").send_keys(contact.address)
        dw.find_element_by_name("mobile").click()
        dw.find_element_by_name("mobile").clear()
        dw.find_element_by_name("mobile").send_keys(contact.mobile)
        dw.find_element_by_name("email").click()
        dw.find_element_by_name("email").clear()
        dw.find_element_by_name("email").send_keys(contact.email)
        # submit contact creation
        dw.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_main_page(self):
        dw = self.app.dw
        dw.find_element_by_link_text("home").click()