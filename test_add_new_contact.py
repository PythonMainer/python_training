# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from contact import Contact

class AddNewContact(unittest.TestCase):
    def setUp(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(30)

    def test_add_new_contact(self):
        dw = self.dw
        self.open_main_page(dw)
        self.login(dw, username='admin', password='secret')
        self.new_create_contact(dw, Contact(firstname='Вадим', middlename='Сергеевич', lastname='Трофимов', nickname='Вадик', address='Москва', mobile='+79503585665', email='1@mail.ru'))
        self.return_main_page(dw)
        self.logout(dw)

    def logout(self, dw):
        dw.find_element_by_link_text("Logout").click()

    def return_main_page(self, dw):
        dw.find_element_by_link_text("home").click()

    def new_create_contact(self, dw, contact):
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

    def login(self, driver, username, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_id("LoginForm").click()
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_main_page(self, driver):
        driver.get("http://localhost/addressbook/")

    def tearDown(self):
        self.dw.quit()


if __name__ == "__main__":
    unittest.main()
