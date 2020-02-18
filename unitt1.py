import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner
from selenium.webdriver.support.wait import WebDriverWait
from file1 import *

class TestCase1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\Suraj.k\\Downloads\\chromedriver_win32\\chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        cls.driver.find_element_by_name("txtUsername").send_keys("Admin")
        cls.driver.find_element_by_name("txtPassword").send_keys("admin123")
        cls.driver.implicitly_wait(1000)
        cls.driver.find_element_by_name("Submit").click()

    def test_homepageTitle(self):
        self.driver.find_element_by_id("menu_admin_viewAdminModule").click()
        self.driver.find_element_by_name("searchSystemUser[userName]").send_keys("hannah.flores")
        drop = Select(self.driver.find_element_by_name("searchSystemUser[userType]"))
        drop.select_by_index(2)
        self.driver.find_element_by_name("searchSystemUser[employeeName][empName]").send_keys("Hannah Flores")
        select1 = Select(self.driver.find_element_by_name("searchSystemUser[status]"))
        select1.select_by_index(1)
        self.driver.find_element_by_name("_search").click()

    def test_AddUser(self):
        self.driver.find_element_by_id("menu_pim_viewPimModule").click()
        self.driver.find_element_by_id("menu_pim_addEmployee").click()
        self.driver.find_element_by_name("firstName").send_keys("Suraj")
        self.driver.find_element_by_name("middleName").send_keys("")
        self.driver.find_element_by_name("lastName").send_keys("Kumar")
        self.driver.find_element_by_name("employeeId").send_keys("a1123")
        self.driver.find_element_by_name("photofile").send_keys("Downloads\\IMG_20200110_122702.jpg")
        self.driver.find_element_by_name("chkLogin").click()
        self.driver.find_element_by_id("btnSave").click()

    def test_search(self):
        pass


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Case Completed")




if __name__ == "__main__":
    # noinspection PyCallingNonCallable
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:\\Users\\Suraj.k\\PycharmProjects\\Python_selenium_project\\Demo'))
