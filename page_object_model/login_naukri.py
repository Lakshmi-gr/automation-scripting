from selenium.webdriver.common.by import By
from page_object_model.searchjob_naukri import Search_job


class Login_page:
    def __init__(self,driver):
        self.driver=driver
        self.Login_page=(By.ID,"login_Layer")
        self.Username_input=(By.XPATH,"//input[@placeholder='Enter your active Email ID / Username']")
        self.password=(By.XPATH,"//input[@type='password']")
        self.Login_button=(By.XPATH,"//button[text()='Login']")




    def login(self):
        self.driver.find_element(*self.Login_page).click()
        self.driver.find_element(*self.Username_input).send_keys("ravitejagaddam0806@gmail.com")
        self.driver.find_element(*self.password).send_keys("Jump2@Pump")
        self.driver.find_element(*self.Login_button).click()
        search_job=Search_job(self.driver)
        return search_job