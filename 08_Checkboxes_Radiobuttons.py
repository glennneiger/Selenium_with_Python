from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Check if the the Radio button is selected
status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print("Radiobutton male checked?: ",status)

# Selects one and print status
driver.find_element_by_xpath("//label[contains(text(),'Male')]").click()
status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print("Radiobutton male checked: ", status)

# Selects Sunday
driver.find_element_by_xpath("//label[contains(text(),'Sunday')]").click()
time.sleep(2)
status = driver.find_element_by_xpath("//input[@id='RESULT_CheckBox-8_0']").is_selected()
print("Sunday is selected ? = ", status)
