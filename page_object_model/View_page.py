import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class profile:
    def __init__(self, driver):
        self.driver=driver
        self.view_tab=(By.XPATH,"//a[text()='View']")
        self.resume=(By.ID, "attachCV")
        self.update_resume=(By.XPATH, "//input[@value='Update resume']")


    def test_view_profile(self):
        self.driver.find_element(*self.view_tab).click()
        scroll_position = 800
        self.driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        try:
            # Wait until file input is present
            file_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.resume)
            )
            time.sleep(3)
            file_input.send_keys("C:/Users/ravit/Downloads/Raviteja_Resume.pdf")  # Put your file path here
            print("✅ File uploaded (path sent).")
            time.sleep(3)

            # Click the 'Update resume' button
            self.driver.find_element(*self.update_resume).click()
            time.sleep(3)
            print("✅ Clicked 'Update resume' button.")

        except Exception as e:
            print("⚠️ Error or timeout:", e)

        finally:
            self.driver.quit()

