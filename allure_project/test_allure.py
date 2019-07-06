from selenium import webdriver
import time
import pytest
import allure
from allure_commons.types import AttachmentType



class TestGoogleSearch:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/Totti10/PycharmProjects/Selenium/drivers/chromedriver.exe")
        driver.implicitly_wait(5)
        driver.set_window_size(1200, 800)
        yield
        time.sleep(5)
        driver.close()
        driver.quit()
        print("Test Completed")

    @allure.feature('Search')
    @allure.story('Open google.com and search for Suzuki')
    @allure.severity('blocker')
    def test_search_suzuki(self, test_setup):
        driver.get("https://www.google.com/?gl=us&hl=en&pws=0&gws_rd=cr")
        driver.find_element_by_name("q").send_keys("Suzuki")
        driver.find_element_by_name("btnK").submit()
        with allure.step('Get screenshot'):
             allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert driver.title == 'Suzuki - Google Search'


    @allure.feature('Search')
    @allure.story('Open google.com and search for Stas')
    @allure.severity('blocker')
    def test_search_stas(self):
        self.driver.get("https://www.google.com/?gl=us&hl=en&pws=0&gws_rd=cr")
        self.driver.find_element_by_name("q").send_keys("Stas")
        self.driver.find_element_by_name("btnK").submit()
        with allure.step('Get screenshot'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


    # def test_teardown():
    #     time.sleep(5)
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed")
