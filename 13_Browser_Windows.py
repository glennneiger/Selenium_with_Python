# Drivers & Exercise Web
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

# Returns the handle onf the current browser
print(driver.current_window_handle)  # CDwindow-5BCC77B34F8157D57449C088AB75E013 - parent window

# Returns all the handles values of opened browsers
handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()  # close only parent browser
