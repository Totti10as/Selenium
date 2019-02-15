from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("../drivers/chromedriver.exe")

driver.get("http://google.com")

time.sleep(5)

driver.quit()

test