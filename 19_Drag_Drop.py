# Drivers & Exercise Web
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

driver.maximize_window()

source_element = driver.find_element_by_xpath("//*[@id='box6']")
target_element = driver.find_element_by_xpath('//*[@id="box106"]')

actions = ActionChains(driver)

# Drag & Drop
actions.drag_and_drop(source_element, target_element).perform()