from selenium import webdriver
from allure_commons.types import AttachmentType

import allure
import time
import pytest


class TestGoogleSearch:

    def setup(self):
        self.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.set_window_size(1200, 800)

    @allure.feaure('Search')
    @allure.story('Open google.com and search for Suzuki')
    @allure.severity('blocker')
    def test_search_suzuki(self):
         self.driver.get("https://www.google.com/?gl=us&hl=en&pws=0&gws_rd=cr")
         self.driver.find_element_by_name("q").send_keys("Suzuki")
         self.driver.find_element_by_name("btnK").submit()
         with allure.step('Get screenshot'):
             allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

    # @allure.feature('Search')
    # @allure.story('Open google.com and search for Stas')
    # @allure.severity('blocker')
    # def test_search_stas(self):
    #     self.driver.get("https://www.google.com/?gl=us&hl=en&pws=0&gws_rd=cr")
    #     self.driver.find_element_by_name("q").send_keys("Stas")
    #     self.driver.find_element_by_name("btnK").submit()
    #     with allure.step('Get screenshot'):
    #         allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)


    def teardown(self):
        time.sleep(5)
        self.driver.close()
        self.driver.quit()
        print("Test Completed")

