from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import HtmlTestRunner
import os.path


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.set_window_size(1200, 800)

    def test_search_suzuki(self):
         self.driver.get("https://www.google.com/?gl=us&hl=en&pws=0&gws_rd=cr")
         self.driver.find_element_by_name("q").send_keys("Suzuki")
         self.driver.find_element_by_name("btnK").submit()

    def test_search_stas(self):
        self.driver.get("https://www.google.com/?gl=us&hl=en&pws=0&gws_rd=cr")
        self.driver.find_element_by_name("q").send_keys("Stas")
        self.driver.find_element_by_name("btnK").submit()

    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Totti10/PycharmProjects/Selenium/reports'))



