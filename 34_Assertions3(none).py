import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")
        # self.assertIsNone(driver) #this will verify if the driver contains some value or not. If it does not contain anything it will pass.

        driver = None
        # self.assertIsNone(driver) #will pass when driver = None
        self.assertIsNotNone(driver)  # Will fail when driver = None


if __name__ == '__main__':
    unittest.main()
