from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")
# driver=webdriver.Firefox(executable_path="C:/DRIVERS/Selenium_drivers/geckodriver-v0.24.0-win64/geckodriver.exe")

driver.get("http://newtours.demoaut.com/")

# tittle of the page
print(driver.title)

# returns url of the page
print(driver.current_url)

# returns the HTML code for the page
print(driver.page_source)

# close the browser
driver.close()

