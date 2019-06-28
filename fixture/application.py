from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def return_main_page(self):
        dw = self.dw
        dw.find_element_by_link_text("home").click()

    def open_main_page(self):
        dw = self.dw
        dw.get("http://localhost/addressbook/")

    def destroy(self):
        self.dw.quit()