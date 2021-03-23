from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\Python27\Scripts\chromedriver.exe")
driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")
driver.maximize_window()
rows=len(driver.find_elements_by_xpath("//*[@id='post-body-5867683659713562481']/div/div[1]/table/tbody/tr"))
cols=len(driver.find_elements_by_xpath("//*[@id='post-body-5867683659713562481']/div/div[1]/table/tbody/tr[1]/th"))
print(rows)
print(cols)

print("Country"+" "+"City"+" "+"Height"+" "+"Built"+" "+"Rank" )
for r in range(2,rows+1):
    for c in range(1,cols+1):
        value=driver.find_element_by_xpath("//*[@id='post-body-5867683659713562481']/div/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value)

driver.close()

