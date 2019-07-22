# Drivers & Exercise Web
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

element = driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")

actions = ActionChains(driver)

# Perform double click on the element (button)
actions.double_click(element).perform()