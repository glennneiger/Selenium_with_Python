# Drivers & Exercise Web
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element_by_xpath("/html/body/div[1]/section/div/div/div/p/span")

actions = ActionChains(driver)

# Perform the right click action
actions.context_click(button).perform()