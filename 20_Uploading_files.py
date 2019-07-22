# Drivers & Exercise Web
from selenium import webdriver
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.switch_to.frame(0)

driver.find_element_by_id("RESULT_FileUpload-11").send_keys("/home/manuel/Imágenes/2019-07-23_(00.02).png")