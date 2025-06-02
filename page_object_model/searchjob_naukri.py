from selenium.webdriver.common.by import By
from page_object_model.View_page import profile

class Search_job:

    def __init__(self,driver):
        self.driver=driver
        self.search_jobpage=(By.XPATH,"//span[text()='Search jobs here']")
        self.Enter_designation=(By.XPATH,"//input[@placeholder='Enter keyword / designation / companies']")
        self.select_designation=(By.XPATH,"//div[@title='QA automation Testing Engineer']")
        self.experience=(By.ID,"experienceDD")
        self.select_experience=(By.XPATH,"//span[text()='3 years']")
        self.enter_location=(By.XPATH,"//input[@placeholder='Enter location']")
        self.select_location=(By.XPATH,"//div[@title='Bengaluru']")
        self.search_button=(By.XPATH,"//span[@class='ni-gnb-icn ni-gnb-icn-search']")


    def searchjob(self):
        self.driver.find_element(*self.search_jobpage).click()
        self.driver.find_element(*self.Enter_designation).send_keys("QA automation")
        self.driver.find_element(*self.select_designation).click()
        self.driver.find_element(*self.experience).click()
        self.driver.find_element(*self.select_experience).click()
        self.driver.find_element(*self.enter_location).send_keys("b")
        self.driver.find_element(*self.select_location).click()
        self.driver.find_element(*self.search_button).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.back()
        view = profile(self.driver)
        return view
