import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import HtmlTestRunner


class TestCase1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\\Suraj.k\\Downloads\\chromedriver_win32\\chromedriver.exe")
        cls.driver.maximize_window()

    def test_homepageTitle(self):
        self.driver.get("https://www.google.com")
        self.driver.maximize_window()
        self.driver.find_element_by_name("q").send_keys("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.find_element_by_name("btnK").submit()
        self.driver.find_element_by_class_name("LC20lb").click()
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")

    def test_LoginPage(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Case Completed")





if __name__ == "__main__":
    # noinspection PyCallingNonCallable
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Suraj.k\\PycharmProjects\\Python Project\\Demo'))