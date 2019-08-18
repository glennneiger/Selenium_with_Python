from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")
driver.get("http://newtours.demoaut.com/mercurywelcome.php")

# driver.save_screenshot("C:/Users/Usuario/PycharmProjects/Selenium_with_Python/Useful_files/screenshots/screenshot_ex_1.png")

driver.get_screenshot_as_file(
    "C:/Users/Usuario/PycharmProjects/Selenium_with_Python/Useful_files/screenshots/screenshot_ex_2.png")
