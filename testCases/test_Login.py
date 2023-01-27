import os

import pytest
from utility.ReadProperties import ReadProperties
from logs.LogGen import LogGen


class TestLogin01:
    url = ReadProperties.getUrl()
    username = ReadProperties.getUserEmail()
    password = ReadProperties.getPassword()
    logger = LogGen.logGen()
    logger.info("------------------ TestLogin01 ------------------ ")

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
