from selenium import  webdriver
import pytest
from pages.loginpage import LoginPage
from pages.homepages import HomePage
from utils import utils as utils
import allure
import moment

@pytest.mark.usefixtures("test_setup")
class Test_login():

    def test_login(self):
        driver=self.driver
        driver.get(utils.URL)
        login=LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_connect()


    def test_logout(self):
        try:
            driver=self.driver
            homepage=HomePage(driver)
            homepage.click_disconnect()
            x= driver.title
            assert x== "ABC"
        except AssertionError as error
            print("assertion error occurred")
            print(error)
            currtime=moment.now().strftime("%d-%m-%Y-%M-%S")
            screenshot="screenshot"+currtime
            allure.attach(self.driver.get_screenshot_as_png(),name= screenshot,attachment_type=allure.attachement_type.PNG)
            raise
        except:
            print("there was an exception")
            raise
        else:
            print("no exceptions occurred")
        finally:
            print("i am inside finally block")
        # driver.find_element_by_id("username").send_keys("user")
        # time.sleep(5)
        # driver.find_element_by_id("password").send_keys("user")
        # time.sleep(5)
        # driver.find_element_by_id("loginBtn").click()
        # time.sleep(5)
        # driver.find_element_by_xpath('//a[contains(text(),"connecter") and @href="#"]').click()
        # time.sleep(10)




