from selenium import webdriver
import unittest
import HtmlTestRunner


class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/DRIVERS/Selenium_drivers/chromedriver_win32/chromedriver.exe")
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM", self.driver.title, "webpage title is not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test completed...")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='C:/Users/Usuario/PycharmProjects/Selenium_with_Python/Reports'))  # Important to get the report it must be included testRunner after unittest.main

# To launch the test do it from terminal using: python testtobeexecuted.py.
# To see the reports open browser in correspondent report file
