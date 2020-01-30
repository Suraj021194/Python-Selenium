from selenium import webdriver
import unittest
import HtmlTestRunner

class orangeHRMTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = "C:\\Users\\suraj\\Desktop\\chromedriver_win32\\chromedriver.exe")
        cls.driver.maximize_window()
        
    def test_homepageTitle(self):
        self.driver.get("https://urncc.org/#/")
        self.assertEqual("Harit App", self.driver.title, "webpage title is not matching")
        
    def test_login(self):
        self.driver.get("https://urncc.org/#/")
        self.driver.find_element_by_id("userName").send_keys("Admin")
        self.driver.find_element_by_class_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.driver.find_element_css_selector
        self.assertEqual("Harit App", self.driver.title, "webpage title is not matching")
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")
        

if __name__ == "__main__":
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = "..\\Python Project\\Reports"))    
        
        
        