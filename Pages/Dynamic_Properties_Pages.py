from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class dynamic_properties:
    def __init__(self,driver):
        self.driver = driver
        self.enable_after_5_Seconds = "enableAfter"
        self.change_color_btn = "colorChange"
        self.visible_after_5_seconds = "visibleAfter"
        self.dynamic_text = "//div[@class='col-12 mt-4 col-md-6']//div//p"

    def check_button_enabled(self):
        element_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.enable_after_5_Seconds)))
        element_btn.click()

    def check_color_change(self):
        original_color = self.driver.find_element(By.ID,self.change_color_btn)
        initial_color = original_color.value_of_css_property("border-color")
        print(initial_color)
        original_color.click()
        secondary_color = original_color.value_of_css_property("border-color")
        print(secondary_color)

    def check_button_visibility(self):
        element_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.visible_after_5_seconds)))
        element_btn.click()


    def verify_text_from_dynamic_ID(self):
        get_text = self.driver.find_element(By.XPATH,self.dynamic_text)
        dy_text = get_text.text
        print(dy_text)
        return dy_text