from selenium.webdriver.common.by import By


class handling_frames:
    def __init__(self,driver):
        self.driver = driver
        self.iframe1 = "frame1"
        self.iframe2 = "frame2"

    def handle_iframe1(self):
        self.driver.switch_to.frame(self.driver.find_element(By.ID,self.iframe1))

    def handle_iframe2(self):
        self.driver.switch_to.frame(self.driver.find_element(By.ID,self.iframe2))