import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def setup():
    from selenium.webdriver.chrome.service import Service
    ser_obj = Service("C:/Users/riyaj/Downloads/chromedriver_win32/chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option('detach', True)
    # ops.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=ser_obj, options=ops)
    yield driver
    time.sleep(3)
    driver.quit()
