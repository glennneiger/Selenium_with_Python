from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

# Get and counts all the link with the tag "a"
links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links present: ", len(links))

# Name the links
for link in links:
    print(link.text)

# Clicking on the link using full link text
# driver.find_element(By.LINK_TEXT, "REGISTER").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click()

driver.stop_client()
