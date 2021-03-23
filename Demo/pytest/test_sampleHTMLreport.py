from selenium import webdriver
import pytest

@pytest.fixture()
def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:\Python27\Scripts\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("Test Completed")

def test_login(test_setup):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    if driver.title=="OrangeHRM":
        assert True
    else:
        assert False