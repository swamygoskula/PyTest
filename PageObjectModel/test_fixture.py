import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver=None
@pytest.fixture
def setup():
    print("start browser")
    global driver
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.quit()
    print("close browser")

def test_1(setup):
    driver.get("https://www.google.co.in/")
    print("Executed test 1")

def test_2(setup):
    driver.get("https://www.facebook.com/")
    print("Executed test 2")

def test_3(setup):
    driver.get("https://www.bing.com/")
    print("Executed test 3")