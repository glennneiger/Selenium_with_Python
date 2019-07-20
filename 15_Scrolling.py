# Drivers & Exercise Web
from selenium import webdriver
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# Maximize window
driver.maximize_window()

# 1. Scrolling down page by pixel
# driver.execute_script("window.scrollBy(0, 1000)", "")

# 2. Scrolling down page by pixel
flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();", flag)

# 3. Scroll until the end of the page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")