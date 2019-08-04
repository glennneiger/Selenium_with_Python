# Drivers & Exercise Web
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe",
                          options=chrome_options)
driver.get("http://demo.automationtesting.in/FileDownload.html")

# This is in case you want to save it somewhere else than the default location
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {"download.default_directory": r"C:\Users\Usuario\Downloads"})

driver.maximize_window()

driver.find_element_by_id("textbox").send_keys("testing download text file")
driver.find_element_by_id("createTxt").click()  # Generate file button
driver.find_element_by_id("link-to-download").click()  # Download link

driver.find_element_by_id("pdfbox").send_keys("testing_pdf")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click

driver.close()
