from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")

driver.get("https://www.amazon.es")

# Capture all the cookies created by the browser
cookies = driver.get_cookies()
print("Cookies total = ", len(cookies))  # print number of cookies being created
print(cookies)  # print all the cookies pairs

# Adding a new cookie to the browser
cookie = {'name': 'Mycookie', 'value': '123456790'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print("Cookies total = ", len(cookies))  # print number of cookies after adding new cookie
print(cookies)  # print all the cookies pairs

# Deleting cookie file
driver.delete_cookie('Mycookie')
cookies = driver.get_cookies()
print("Cookies total = ", len(cookies))  # print number of cookies after deleting the cookie
print(cookies)  # print all the cookies pairs

# Deleting cookie file
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("Cookies total = ", len(cookies))  # expected output = 0
