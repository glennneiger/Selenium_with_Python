from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)

# HOW TO SELECT OPTIONS (

# Select by visible text
drp.select_by_visible_text('Morning')
# # Select by index
drp.select_by_index(2) # Afternoon
# Select by value
drp.select_by_value("Radio-2") # Evening


# COUNT NUMBER OF OPTIONS
print(len(drp.options))

# CAPTURE ALL THE OPTIONS AND PRINT THEM AS OUTPUT

all_options = drp.options
for option in all_options:
    print(option.text)


