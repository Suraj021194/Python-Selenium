from selenium import webdriver
import unittest
import HtmlTestRunner

class orangeHRMTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = "C:\\Users\\suraj\\Desktop\\chromedriver_win32\\chromedriver.exe")
        cls.driver.maximize_window()
        
    def test_homepageTitle(self):
        self.driver.get("https://www.geeksforgeeks.org/")
        self.assertEqual("GeeksforGeeks | A computer science portal for geeks", self.driver.title, "webpage title is not matching")
        
    def test_login(self):
        self.driver.get("https://www.geeksforgeeks.org/")
        self.driver.find_element_by_class_name("ButtonContribute").click()
        self.driver.find_element_by_class_name("active").click()
        self.assertEqual("GFG Courses | Practice | GeeksforGeeks", self.driver.title, "webpage title is not matching")
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")
        

if __name__ == "__main__":
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = "..\\Python Project\\Reports"))    
        