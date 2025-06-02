from py2store.parse_format import search
from selenium import webdriver
from page_object_model.login_naukri import Login_page
from My_Tests.Utils.Logger import get_logger
import time

logger = get_logger(__name__)

def test_upload_resume(driver):
    logger.info("Logging into the MyNaukri.com and updating the resume")

    #driver=webdriver.Chrome()
    driver.get("https://www.naukri.com/")
    driver.implicitly_wait(20)

    Login = Login_page(driver)
    search = Login.login()
    view = search.searchjob()
    view.test_view_profile()

time.sleep(3)