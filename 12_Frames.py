from selenium import webdriver
import time

# Drivers & Exercise Web
driver = webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")

# 1. Top left click
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()

# Needed to use .default_content to get out of the first frame
driver.switch_to.default_content()
time.sleep(3)

# 2. Bottom left click
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
driver.switch_to.default_content()
time.sleep(3)

# 3. Main container frame

driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html[1]/body[1]/div[1]/ul[1]/li[5]").click()

# Notes: switch_to.frame will work on (name) and (id)
