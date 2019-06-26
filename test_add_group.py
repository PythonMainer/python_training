# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(30)

    def test_add_group(self):
        dw = self.dw
        self.open_main_page(dw)
        self.login(dw, username='admin', password='secret')
        self.open_group_page(dw)
        self.create_group(dw, Group(name='group', header='2', footer='2'))
        self.return_group_page(dw)
        self.logout(dw)

    def test_add_empty_group(self):
        dw = self.dw
        self.open_main_page(dw)
        self.login(dw, username='admin', password='secret')
        self.open_group_page(dw)
        self.create_group(dw, Group(name='group', header='', footer=''))
        self.return_group_page(dw)
        self.logout(dw)

    def return_group_page(self, dw):
        dw.find_element_by_link_text("group page").click()

    def logout(self, dw):
        dw.find_element_by_link_text("Logout").click()

    def create_group(self, dw, group):
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

    def open_group_page(self, dw):
        dw.find_element_by_link_text("groups").click()

    def login(self, dw, username, password):
        dw.find_element_by_name("user").click()
        dw.find_element_by_name("user").clear()
        dw.find_element_by_name("user").send_keys(username)
        dw.find_element_by_id("LoginForm").click()
        dw.find_element_by_name("pass").click()
        dw.find_element_by_name("pass").clear()
        dw.find_element_by_name("pass").send_keys(password)
        dw.find_element_by_xpath("//input[@value='Login']").click()

    def open_main_page(self, dw):
        dw.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.dw.quit()


if __name__ == "__main__":
    unittest.main()
