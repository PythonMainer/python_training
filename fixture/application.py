from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(30)
        self.session = SessionHelper(self)

    def return_group_page(self):
        dw = self.dw
        dw.find_element_by_link_text("group page").click()

    def create_group(self, group):
        dw = self.dw
        self.open_group_page()
        # init group creation
        dw.find_element_by_name("new").click()
        # fill group form
        dw.find_element_by_name("group_name").click()
        dw.find_element_by_name("group_name").clear()
        dw.find_element_by_name("group_name").send_keys(group.name)
        dw.find_element_by_name("group_header").click()
        dw.find_element_by_name("group_header").clear()
        dw.find_element_by_name("group_header").send_keys(group.header)
        dw.find_element_by_name("group_footer").click()
        dw.find_element_by_name("group_footer").clear()
        dw.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        dw.find_element_by_name("submit").click()
        self.return_group_page()

    def open_group_page(self):
        dw = self.dw
        dw.find_element_by_link_text("groups").click()

    def open_main_page(self):
        dw = self.dw
        dw.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.dw.quit()