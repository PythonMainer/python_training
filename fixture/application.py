from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:

    def __init__(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_main_page(self):
        dw = self.dw
        dw.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.dw.quit()