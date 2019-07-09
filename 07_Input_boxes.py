from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# Count how many input boxes are present in the page
inputboxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print(f'Inputboxes = {len(inputboxes)}')

# Print if the dashboards are displayed - enabled or not
status = driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print("Displayed or not = ", status)
status = driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
print("Enabled or not = ", status)

# Provide value into the text box

driver.find_element(By.ID, 'RESULT_TextField-1').send_keys("pavan")
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("kumar")

driver.stop_client()