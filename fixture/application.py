from selenium import webdriver


class Application:

    def __init__(self):
        self.dw = webdriver.Firefox()
        self.dw.implicitly_wait(30)

    def return_group_page(self):
        dw = self.dw
        dw.find_element_by_link_text("group page").click()

    def logout(self):
        dw = self.dw
        dw.find_element_by_link_text("Logout").click()

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

    def login(self, username, password):
        dw = self.dw
        self.open_main_page()
        dw.find_element_by_name("user").click()
        dw.find_element_by_name("user").clear()
        dw.find_element_by_name("user").send_keys(username)
        dw.find_element_by_id("LoginForm").click()
        dw.find_element_by_name("pass").click()
        dw.find_element_by_name("pass").clear()
        dw.find_element_by_name("pass").send_keys(password)
        dw.find_element_by_xpath("//input[@value='Login']").click()

    def open_main_page(self):
        dw = self.dw
        dw.get("http://localhost/addressbook/group.php")

    def destroy(self):
        self.dw.quit()