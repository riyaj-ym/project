import os

import pytest
from utility.ReadProperties import ReadProperties
from logs.LogGen import LogGen
from PageObjectModel.LoginPage import LoginPage


class TestLogin101:
    url = ReadProperties.getUrl()
    username = ReadProperties.getUserEmail()
    password = ReadProperties.getPassword()
    logger = LogGen.logGen()
    logger.info("------------------ TestLogin101 ------------------ ")

    @pytest.mark.retesting
    def test_url(self, setup):
        self.logger.info("------------------ Testing website url ------------------ ")
        driver = setup
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(self.url)
        exp_title = "Your store. Login"
        act_title = driver.title

        if exp_title == act_title:
            self.logger.info("------------------ website url testing got passed ------------------ ")
            assert True
        else:
            self.logger.info("------------------ website url testing got failed ------------------ ")
            driver.save_screenshot(os.getcwd() + "/screenshots/test_url.png")
            assert False

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("------------------ Testing Home Page Title(Login Test) ------------------ ")
        driver = setup
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(self.url)
        lp = LoginPage(driver)
        lp.setUserEmail(self.username)
        lp.setUserPassword(self.password)
        lp.clickLogin()
        actTitle = driver.title

        if actTitle == "Dashboard / nopCommerce administration":
            self.logger.info("------------------ Home Page Title(Login Test) Passed ------------------")
            assert True

        else:
            self.logger.info("------------------ Home Page Title(Login Test) Failed ------------------")
            driver.save_screenshot(os.getcwd() + "/screenshots/test_homePageTitle.png")
            assert False
