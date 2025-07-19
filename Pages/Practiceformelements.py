import re
import datetime
import os
import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class practiceform:
    def __init__(self,driver):
        self.driver = driver
        self.firstname_id = "firstName"
        self.lastname_id = "lastName"
        self.email_id = "userEmail"
        self.gender_xpath = "//label[normalize-space()='Male']"
        self.mobile_num_id = "userNumber"
        self.date_id = "dateOfBirthInput"
        self.subject_xpath = "subjectsInput"
        self.hobbies = "(//label[@for='hobbies-checkbox-1'])[1]"
        self.upload_picture = "uploadPicture"
        self.current_address = "currentAddress"
        self.select_state = "(//div[@class=' css-tlfecz-indicatorContainer'])[1]"
        self.haryana_id = "react-select-3-option-1"
        self.select_city = "//*[@id='city']/div/div[1]/div[1]"
        self.panipat = "react-select-4-option-1"
        self.submit = "submit"

    def rgb_to_hex(self,rgb):
        return '%02x%02x%02x' %rgb

    def enter_firstname(self,fname):
        assert "Student Registration Form" in self.driver.page_source
        time.sleep(2)
        self.driver.find_element(By.ID, self.firstname_id).clear()
        self.driver.find_element(By.ID,self.firstname_id).send_keys(fname)

    def identify_color(self):
        time.sleep(2)
        rgb1 = self.driver.find_element(By.ID,self.firstname_id).value_of_css_property("border-color")
        rgb = self.driver.find_element(By.ID, self.lastname_id).value_of_css_property("border-color")
        rgb2 = self.driver.find_element(By.XPATH, self.gender_xpath).value_of_css_property("border-color")
        rgb3 = self.driver.find_element(By.ID, self.email_id).value_of_css_property("border-color")
        rgb4 = self.driver.find_element(By.ID, self.mobile_num_id).value_of_css_property("border-color")
        print(rgb1,rgb2,rgb3,rgb,rgb4)
        # self.rgb_to_hex(rgb1)

    def identify_lastname_color(self):
        rgb = self.driver.find_element(By.ID,self.lastname_id).value_of_css_property("border-color")
        print(rgb)


    def identify_gender_color(self):
        rgb2 = self.driver.find_element(By.XPATH, self.gender_xpath).value_of_css_property("border-color")
        print(rgb2)


    def enter_lastname(self,lname):
        self.driver.find_element(By.ID, self.lastname_id).clear()
        self.driver.find_element(By.ID,self.lastname_id).send_keys(lname)

    def enter_email(self,email):
        # self.driver.find_element(By.ID, self.email_id).clear()
        self.driver.find_element(By.ID,self.email_id).send_keys(email)

    def identify_email_color(self):
        rgb3 = self.driver.find_element(By.ID, self.email_id).value_of_css_property("border-color")
        print(rgb3)


    def select_gender(self):
        self.driver.find_element(By.XPATH,self.gender_xpath).click()

    def enter_mobile(self,num):
        self.driver.find_element(By.ID, self.mobile_num_id).clear()
        self.driver.find_element(By.ID,self.mobile_num_id).send_keys(num)

    def identify_phone_color(self):
        rgb4 = self.driver.find_element(By.ID, self.mobile_num_id).value_of_css_property("border-color")
        print(rgb4)

    def select_date(self):
        now = datetime.datetime.now()
        tday = now.strftime("%m-%d-%Y")
        self.driver.find_element(By.ID,self.date_id).send_keys(tday)
        self.driver.find_element(By.ID, self.date_id).send_keys(Keys.ENTER)

    def enter_subject(self,sub):
        self.driver.find_element(By.ID,self.subject_xpath).send_keys(sub)
        self.driver.find_element(By.ID, self.subject_xpath).send_keys(Keys.ENTER)


    def select_hobbies(self):
        hob = self.driver.find_element(By.XPATH,self.hobbies)
        self.driver.execute_script("arguments[0].click()",hob)

    def enter_picture(self):
        path = os.getcwd()
        element = self.driver.find_element(By.ID,self.upload_picture)
        self.driver.execute_script("arguments[0].style.display = 'block';", element)
        path1 = os.path.abspath(path + r'/Tests/Pictures/new1.jpg')
        element.send_keys(path1)

    def enter_currentaddress(self,add):
        self.driver.find_element(By.ID, self.current_address).clear()
        self.driver.find_element(By.ID,self.current_address).send_keys(add)

    def click_state(self):
        stat = self.driver.find_element(By.XPATH,self.select_state)
        self.driver.execute_script("arguments[0].scrollIntoView();", stat)
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(stat))
        element.click()
        sstate = self.driver.find_element(By.ID,self.haryana_id).click()


    def click_city(self):
        city = self.driver.find_element(By.XPATH,self.select_city).click()
        # self.driver.execute_script("arguments[0].click()", city)
        time.sleep(2)
        scity = self.driver.find_element(By.ID,self.panipat).click()
        # self.driver.execute_script("arguments[0].click()", scity)

    def click_submit(self):
        submitbtn = self.driver.find_element(By.ID,self.submit)
        self.driver.execute_script("arguments[0].click()",submitbtn)