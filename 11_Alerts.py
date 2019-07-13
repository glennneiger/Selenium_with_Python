from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath("//button[contains(text(),'Copy Text')]").click()

time.sleep(5)

# Closes alert window using ok button
# Won´t work on the page above since alert window is substituted by another one.

# driver.switch_to.alert.accept

# Closes alert window using cancel
# driver.switch_to.alert.dismiss()

# Use this one to close cookie alert button
driver.find_element_by_xpath("//a[@id='cookieChoiceDismiss']").click()
driver.switch_to.default_content
