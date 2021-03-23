from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\Python27\Scripts\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")
driver.maximize_window()
#time.sleep(5)
#scroll down the page by pixel
#driver.execute_script("window.scrollBy(0,1000)","")
#scroll down page till element visible
#flag=driver.find_element_by_xpath("//*[@id='main']/div[9]/a")
#driver.execute_script("arguments[0].scrollIntoView();",flag)
#time.sleep(5)
#scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
driver.close()
