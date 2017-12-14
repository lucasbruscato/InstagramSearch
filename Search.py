
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:/Program Files (x86)/Mozilla Firefox/firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)
# driver = webdriver.Chrome()

driver.get("https://www.instagram.com/")

time.sleep(5)

elem = driver.find_element_by_name("emailOrPhone")
elem.send_keys("teste")












# driver.execute_script("https://www.instagram.com/static/bundles/Vendor.js/4cb68b6771d9.js:1")
