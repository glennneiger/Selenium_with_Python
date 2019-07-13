# Drivers & Exercise Web
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")
driver.get("http://www.materialeslosandes.com/vigasipn.html")

# Count number of rows present in the table
rows = len(driver.find_elements_by_xpath("/html/body/p[2]/table/tbody/tr"))

# Count number of columns
cols = len(driver.find_elements_by_xpath("/html/body/p[2]/table/tbody/tr[1]/td"))

# Print total of first set of rows and cols related
print("rows = ", rows)
print("cols =", cols)

# Print name of columns
print("CALIDAD" + "  " + "% C(MAX)" + "  " + "% Mn(MAX)" + "  " + "% P(MAX)" + "  " + "% S(MAX)")

# Table iteration, print outupt as table

for r in range(2, rows + 1):
    for c in range(1, cols + 1):
        value = driver.find_element_by_xpath("/html/body/p[2]/table/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(value, end='        ')
    print()
