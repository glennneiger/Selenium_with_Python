from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.com/")

# Clicks once on flight button
driver.find_element(By.ID, "tab-flight-tab-hp").click()

# Origin & Destination
time.sleep(5)
driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("NYC")
time.sleep(5)
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("SFO")

# Enter departing and returning dates
driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("12/11/2019")
driver.find_element(By.ID, "flight-returning-hp-flight").clear()
time.sleep(5)
returnDate = driver.find_element(By.ID, "flight-returning-hp-flight")
returnDate.send_keys(Keys.CONTROL + "a", Keys.DELETE)
returnDate.send_keys("15/11/2019")

# Click on the search button
driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()

# Explicit Waits
wait = WebDriverWait(driver, 10)

wait.until(EC.element_to_be_clickable(By.XPATH, "//*[@id='stopFilter_stops-0']")).click()

time.sleep(3)

driver.quit()
