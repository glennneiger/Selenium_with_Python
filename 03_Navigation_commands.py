from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")

driver.get("http://newtours.demoaut.com")
print(driver.title) # 1 (FR)

driver.get("http://pavantestingtools.blogspot.in/")
print(driver.title) # 2(SDET)

time.sleep(2)

# Going back from page 2 to 1
driver.back()
time.sleep(2)
print(driver.title) # 1(FR)

# Going forwards from page 1 to 2
driver.forward()
time.sleep(2)
print(driver.title) #2 (SDET)

driver.quit()