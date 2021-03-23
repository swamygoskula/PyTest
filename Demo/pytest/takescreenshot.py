from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Python27\Scripts\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
#driver.save_screenshot("E:\screenshots\homepage.png")
driver.get_screenshot_as_file("E:\screenshots\homepage2.jpg")
driver.close()