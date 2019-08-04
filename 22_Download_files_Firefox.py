from selenium import webdriver

fp = webdriver.FirefoxProfile()  # this is the equivalent to chromeoptions (options) in Chrome
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "C:/Downloadedfiles")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(executable_path="C:/DRIVERS/Selenium_drivers/geckodriver-v0.24.0-win64/geckodriver.exe",
                           firefox_profile=fp)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

driver.find_element_by_id("textbox").send_keys("testing download text file")
driver.find_element_by_id("createTxt").click()  # Generate file button
driver.find_element_by_id("link-to-download").click()  # Download link

driver.find_element_by_id("pdfbox").send_keys("testing_pdf")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click

driver.close()
