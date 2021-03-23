from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Python27\Scripts\chromedriver.exe")
driver.get("https://selfcare.actcorp.in/web/hyd/aboutus?id=lnk1")
driver.find_element_by_xpath("//*[@id='banner']/div[1]/a[6]").click()
print(driver.current_window_handle)
handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="ACT Fibernet - Home | Facebook":
        driver.close()

driver.quit()