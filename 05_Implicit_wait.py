from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

# Wait up until "x" seconds until the next step is executed if an element is not found
driver.implicitly_wait(5)

# Verify title of the page
assert "Welcome: Mercury Tours" in driver.title

# Send credentials and click on login
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")

driver.find_element_by_name("login").click()

driver.quit()

