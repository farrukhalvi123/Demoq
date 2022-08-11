from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class login:
    def __init__(self,driver):
        self.driver = driver
        self.email_field_name = "email"
        self.pwd_field_name = "password"
        self.login_btn_name = "submit"

    def enter_email(self,email_id):
        self.driver.find_element(By.NAME,self.email_field_name).send_keys(email_id)

    def enter_password(self, pwd):
        self.driver.find_element(By.NAME, self.pwd_field_name).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(By.NAME,self.login_btn_name).click()
