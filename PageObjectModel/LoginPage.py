from selenium.webdriver.common.by import By


class LoginPage:
    inputBox_UserEmail_ID = "Email"
    inputBox_Password_ID = "Password"
    button_Login_XPATH = '//button[normalize-space()="Log in"]'
    link_Logout_XPATH = '//*[@id="navbarText"]/ul/li[3]/a'

    def __init__(self, driver):
        self.driver = driver

    def setUserEmail(self, username):
        self.driver.find_element(By.ID, self.inputBox_UserEmail_ID).clear()
        self.driver.find_element(By.ID, self.inputBox_UserEmail_ID).send_keys(username)

    def setUserPassword(self, password):
        self.driver.find_element(By.ID, self.inputBox_Password_ID).clear()
        self.driver.find_element(By.ID, self.inputBox_Password_ID).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_Login_XPATH).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_Logout_XPATH).click()
