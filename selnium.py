from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


print("sample test case started")
driver = webdriver.Chrome(executable_path="C:\\Users\\Suraj.k\\Downloads\\chromedriver_win32\\chromedriver.exe")

#maximize the window size
driver.maximize_window()
#navigate to the url
driver.get("https://www.google.com/")
#identify the Google search text box and enter the value
driver.find_element_by_name("q").send_keys("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
# time.sleep(3)
#click on the Google search button
driver.find_element_by_name("btnK").submit()
time.sleep(3)
driver.find_element_by_class_name("LC20lb").click()
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_name("Submit").click()
driver.find_element_by_id("menu_admin_viewAdminModule").click()
driver.find_element_by_id("menu_admin_UserManagement").click()
driver.find_element_by_id("menu_admin_viewSystemUsers").click()
driver.find_element_by_name("searchSystemUser[userName]").send_keys("a1123")
dropdown = Select(driver.find_element_by_id("searchSystemUser_userType"))
dropdown.select_by_index(2)
driver.find_element_by_id("searchSystemUser_employeeName_empName").send_keys("Fiona Grace")
select = Select(driver.find_element_by_id("searchSystemUser_status"))
select.select_by_index(1)

driver.find_element_by_id("searchBtn").click()

# driver.switch_to.window(driver.find_element_by_link_text("saveSystemUser?userId=18")).click()
driver.find_element_by_name("btnAdd").click()
select1 = Select(driver.find_element_by_name("systemUser[userType]"))
select1.select_by_index(1)
driver.find_element_by_id("systemUser_employeeName_empName").send_keys("Fiona Grace")
driver.find_element_by_name("systemUser[userName]").send_keys("02suraj45")
select2 = Select(driver.find_element_by_name("systemUser[status]"))
select2.select_by_index(0)
driver.find_element_by_name("systemUser[password]").send_keys("suraj123")
driver.find_element_by_name("systemUser[confirmPassword]").send_keys("suraj123")
driver.find_element_by_name("btnSave").click()
#close the browser
#driver.close()
driver.find_element_by_id("menu_pim_viewPimModule").click()
driver.find_element_by_id("menu_pim_viewEmployeeList").click()

print("sample test case successfully completed")