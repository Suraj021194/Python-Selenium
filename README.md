# Python-Selenium
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\suraj\\Desktop\\Python\\Python\\chromedriver_win32\\chromedriver")
driver.maximize_window()
driver.get("https://www.amazon.in//")
print(driver.title)
print(driver.current_url)
driver.find_element_by_class_name("nav-line-3").click()
# driver.get("https://www.amazon.in/ap/sign-in")
print(driver.title)
print(driver.current_url)
driver.minimize_window()
# driver.back()
driver.refresh()
# driver.close()
