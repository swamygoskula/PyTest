#right click

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Python27\Scripts\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

button=driver.find_element_by_id("menu_admin_viewAdminModule")  ##store the variable in this element

actions=ActionChains(driver)
actions.context_click(button). perform()

#double click

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\Python27\Scripts\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

element=driver.find_element_by_id("menu_admin_viewAdminModule")  ##store the variable in this element

actions=ActionChains(driver)
actions.double_click(element). perform()
