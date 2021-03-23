from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Python27\Scripts\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.switch_to_frame()
driver.find_element_by_id("//*[@id="txtPassword"]").send_keys("E:\How to Build AI assistant like JARVIS using Python\[@BROOKLYN_ARMY]How to Build AI assistant like JARVIS using Python.README.TXT")
