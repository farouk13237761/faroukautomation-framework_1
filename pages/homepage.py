class HomePage():
    import sys
    sys.path.append('/path/to/Code/POM/')

    def __init__(self,driver):
        self.driver=driver
        self.button_disconnect_xpath='//a[contains(text(),"connecter") and @href="#"]'
    def click_disconnect(self):
        self.driver.find_element_by_xpath(self.button_disconnect_xpath).click()
