
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# from selenium.webdriver.common.keys import Keys

binary = FirefoxBinary('C:/Program Files (x86)/Mozilla Firefox/firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)

driver.get("https://www.instagram.com/")

# webdriver.JavascriptExecutor.executeScript("static/bundles/4cb68b6771d9.js")
# driver.execute_script("static/bundles/4cb68b6771d9.js")

# driver.find_element_by_partial_link_text('a login').send_keys(Keys.RETURN)

# driver.find_element_by_css_selector('p._g9ean').send_keys(Keys.RETURN)

# JavascriptExecutor js = (JavascriptExecutor) driver;
# js.executeScript("window.Search();");

# js.executeScript("static/bundles/4cb68b6771d9.js");





