from selenium import webdriver
import unittest
import HtmlTestRunner

class HRMORG(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = "C:\\Users\\suraj\\Desktop\\chromedriver_win32\\chromedriver.exe") 
        cls.driver.maximize_window()
        
    def test_homePage(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM", self.driver.title, "Webpage has no title")
        
        
    def test_login(self):
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Forgot your password?").click()
        # self.driver.find_element_by_name("securityAuthentication[userName]").send_keys("Admin")
        # self.driver.find_element_by_class_name("searchValues").click()
        # self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM", self.driver.title, "webpage has no title")    
    
    # @classmethod      
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #     print("Test is complete")
        

if __name__ == "__main__":
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner("..//Python Project//Reports"))
    