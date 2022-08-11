from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class draganddropclass:
    def __init__(self,driver):
        self.driver = driver
        self.simple_tab_id = "droppableExample-tab-simple"
        self.accept_tab_id = "droppableExample-tab-accept"
        self.prevent_prop_tab = "droppableExample-tab-preventPropogation"
        self.revert_Draggable = "droppableExample-tab-revertable"
        self.dragmebox_id = "draggable"
        self.dropatme_id = "droppable"
        self.acceptablebox_id = "(//div[@class='drag-box mt-4 ui-draggable ui-draggable-handle'])[2]"
        self.notacceptablebox_id = "(//div[@class='drag-box mt-4 ui-draggable ui-draggable-handle'])[3]"
        self.dropbox2_id = "(//div[@class='drop-box ui-droppable'])[2]"
        self.dragbox3 = "dragBox"
        self.outerdrop = "notGreedyDropBox"
        self.innerdrop = "notGreedyInnerDropBox"
        self.outerdropgreedy = "greedyDropBox"
        self.innerdropgreedy = "greedyDropBoxInner"
        self.willrevert = "revertable"
        self.notrevert = "notRevertable"
        self.dropbox4_id = "droppable"

    def click_simple(self):
        self.driver.find_element(By.ID,self.simple_tab_id).click()

    def click_accept(self):
        self.driver.find_element(By.ID, self.accept_tab_id).click()

    def click_prev_prop(self):
        self.driver.find_element(By.ID, self.prevent_prop_tab).click()

    def click_revert_drag(self):
        self.driver.find_element(By.ID,self.revert_Draggable).click()

    def drag_and_drop(self):
        drag = self.driver.find_element(By.ID,self.dragmebox_id)
        drop = self.driver.find_element(By.ID,self.dropatme_id)
        action = ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
    def dragacceptable(self):
        dragaccept = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.acceptablebox_id)))
        droppable = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.dropbox2_id)))
        action = ActionChains(self.driver)
        action.drag_and_drop(dragaccept,droppable).perform()

    def notacceptable(self):
        dragaccept = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.notacceptablebox_id)))
        droppable = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.dropbox2_id)))
        action = ActionChains(self.driver)
        action.drag_and_drop(dragaccept, droppable).perform()

    def Not_Greedy_Prevent_Propogation_Outter(self):
        dragmebox = self.driver.find_element(By.ID,self.dragbox3)
        outerdrop = self.driver.find_element(By.ID,self.outerdrop)
        action = ActionChains(self.driver)
        action.drag_and_drop(dragmebox,outerdrop)

    def Not_Greedy_Prevent_Propogation_Inner(self):
        dragmebox = self.driver.find_element(By.ID, self.dragbox3)
        innerdrop = self.driver.find_element(By.ID,self.outerdrop)
        action = ActionChains(self.driver)
        action.drag_and_drop(dragmebox, innerdrop)

    def Greedy_prevent_propogation_Outter(self):
        dragmebox = self.driver.find_element(By.ID, self.dragbox3)
        innerdrop = self.driver.find_element(By.ID, self.outerdropgreedy)
        action = ActionChains(self.driver)
        action.drag_and_drop(dragmebox, innerdrop)

    def Greedy_prevent_propogation_Inner(self):
        dragmebox = self.driver.find_element(By.ID, self.dragbox3)
        innerdrop = self.driver.find_element(By.ID, self.innerdropgreedy)
        action = ActionChains(self.driver)
        action.drag_and_drop(dragmebox, innerdrop)

    def check_willrevert(self):
        revertbox = self.driver.find_element(By.ID,self.willrevert)
        location = revertbox.location
        print(location)
        dropbox = self.driver.find_element(By.ID,self.dropbox4_id)
        action = ActionChains(self.driver)
        action.drag_and_drop(revertbox, dropbox)
        rgb = dropbox.value_of_css_property("border-color")
        print(rgb)
        print(location)






