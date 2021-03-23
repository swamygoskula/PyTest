import pytest
from selenium import webdriver
from PageObjectModel.LoginPage import LoginPage

class Test_001_Login:
    baseURL="https://opensource-demo.orangehrmlive.com/"
    username="Admin"
    password="admin123"

    def Test_Homepagetitle(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="OrangeHRM":
            assert True
        else:
            assert False

    def Test_Login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.driver.close()
        if act_title=="OrangeHRM":
            assert True
        else:
            False

