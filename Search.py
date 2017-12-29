
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('C:/Program Files (x86)/Mozilla Firefox/firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)

driver.get("https://www.instagram.com/")

time.sleep(5)

elem = driver.find_element_by_name("emailOrPhone")
elem.send_keys(Keys.TAB * 7)

currentElement = driver.switch_to.active_element

currentElement.send_keys(Keys.ENTER)

time.sleep(2)

currentElement = driver.switch_to.active_element

currentElement.send_keys("viagemprofimdomundo@gmail.com")
currentElement.send_keys(Keys.TAB)

currentElement = driver.switch_to.active_element

currentElement.send_keys("42Asimov")
currentElement.send_keys(Keys.TAB * 2)

currentElement = driver.switch_to.active_element

currentElement.send_keys(Keys.ENTER)

time.sleep(4)

# elem = driver.find_elements_by_class_name("_avvq0 _o716c")

# elem = driver.find_element_by_class_name('Search')

# elem.sendKeys("#teste")


