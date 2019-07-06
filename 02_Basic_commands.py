from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome driver
driver=webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

# tittle of the page
print(driver.title)

# returns url of the page
print(driver.current_url)

# Find an element by Xpath and click
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

# Waits x seconds before clicking
time.sleep(5)

# Will close all windows
driver.quit()