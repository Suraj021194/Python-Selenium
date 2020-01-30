from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
# from selenium.webdriver.support import Select

driver = webdriver.Chrome("C:\\Users\\suraj\\Desktop\\chromedriver_win32\\chromedriver.exe")
driver.get("https://realpython.com/modern-web-automation-with-python-and-selenium/")
driver.maximize_window()
driver.find_element_by_id("navbarDropdownLibrary").click()
driver.find_element_by_class_name("dropdown-item").click()
driver.back()
driver.forward()
a = driver.find_element_by_name("q")
a.clear()
a.send_keys("numpy")
a.submit()
driver.back()
a = driver.find_element_by_id("navbarDropdownLibrary")
action = ActionChains(driver)
action.context_click(a).perform()
driver.execute_script("window.open('https://www.twitter.com', 'new window')")
driver.switch_to_window(driver.window_handles[0])
driver.get("https://realpython.com/products/sublime-python/")
driver.execute_script("window.open('https://www.youtube.com/watch?v=cBwoSD45F6g', new window)")

# action = ActionChains(driver)
# action.move_to_element(a).click().perform()

