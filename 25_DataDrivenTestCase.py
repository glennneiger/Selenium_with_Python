import XL_Utils
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")
driver.get("http://newtours.demoaut.com")

driver.maximize_window()

path = "C://Users/Usuario/PycharmProjects/Selenium_with_Python/Useful_files/Login1.xlsx"

rows = XL_Utils.getColumnCount(path, 'Hoja1')

for r in range(2, rows + 1):
    username = XL_Utils.readData(path, "Hoja1", r, 1)
    password = XL_Utils.readData(path, "Hoja1", r, 2)

    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)

    driver.find_element_by_name("login").click()

    if driver.title == "Find a Flight: Mercury Tours:":
        print("test has passed")
        XL_Utils.writeData(path, "Hoja1", r, 3, "test passed")
    else:
        print("test failed")
        XL_Utils.writeData(path, "Hoja1", r, 3, "test failed")

    driver.find_element_by_link_text("Home").click()
