class LoginPage():
    import sys
    sys.path.append('/path/to/Code/POM/')
    def __init__(self,driver):
        self.driver=driver
        self.username_textbox_id="username"
        self.password_textbox_id="password"
        self.button_connect_id="loginBtn"

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys("username")


    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys("password")

    def click_connect(self):
        self.driver.find_element_by_id(self.button_connect_id).click()

