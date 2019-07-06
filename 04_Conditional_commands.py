from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")

driver.get("http://newtours.demoaut.com")

user_ele = driver.find_element_by_name("userName")

# Returns true / false based on element status
print(user_ele.is_displayed())

# Returns T/F depending if element is enabled
print(user_ele.is_enabled())

pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

# Enter username
user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")

driver.find_element_by_name("login").click()

# Locates roundtrip radio button
roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")

# Checks if roundtrip radio button is selected
print("status of round trip radio button", roundtrip_radio.is_selected())

# Same thing for one trip radio button
onetrip_radio = driver.find_element_by_css_selector("input[value=oneway]")
print("status of one way trip radio button", onetrip_radio.is_selected())


driver.quit()