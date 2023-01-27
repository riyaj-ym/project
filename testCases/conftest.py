import time
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup(browser):
    if browser == "edge":
        from selenium.webdriver.edge.service import Service
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        ser_obj = Service(EdgeChromiumDriverManager().install())
        ops = webdriver.EdgeOptions()
        ops.add_experimental_option('detach', True)
        ops.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Edge(service=ser_obj, options=ops)
        yield driver
        time.sleep(3)
        driver.quit()

    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        from webdriver_manager.firefox import GeckoDriverManager
        ser_obj = Service(GeckoDriverManager().install())
        ops = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=ser_obj, options=ops)
        yield driver
        time.sleep(3)
        driver.quit()

    else:
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        ser_obj = Service(ChromeDriverManager().install())
        ops = webdriver.ChromeOptions()
        ops.add_experimental_option('detach', True)
        ops.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(service=ser_obj, options=ops)
        yield driver
        time.sleep(3)
        driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
