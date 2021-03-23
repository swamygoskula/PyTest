import XLUtils
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Python27\Scripts\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
path="E:/Robot/Book2.xlsx"

rows=XLUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username=XLUtils.readData(path,"Sheet1",r,1)
    password=XLUtils.readData(path,"Sheet1",r,2)
    driver.find_element_by_id("txtUsername").send_keys(username)
    driver.find_element_by_id("txtPassword").send_keys(password)
    driver.find_element_by_id("btnLogin").click()

    if driver.title=="OrangeHRM":
        print("Test passed")
        XLUtils.writeData(path,"Sheet1",r,3,"Test passed")
    else:
        print("Test failed")
        XLUtils.writeData(path,"Sheet1",r,3,"Test failed")
    driver.find_element_by_id("welcome").click()
    driver.find_element_by_xpath("//*[@id='welcome-menu']/ul/li[2]/a").click()