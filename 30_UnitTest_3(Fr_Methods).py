import unittest


def setUpModule():  # will be executed before executing any class or any method present in the test class
    print("setUpModule")


def tearDownModule():  # will be executed after executing any class or any method present in the test class
    print("tearDownModule")


class AppTesting(unittest.TestCase):

    @classmethod
    def setUp(self):  # Will execute BEFORE each of the following 4 methods
        print("This is login test")

    @classmethod
    def tearDown(self):  # Will execute AFTER each of the following 4 methods
        print("This is logout test")

    @classmethod
    def setUpClass(cls):  # Will execute once when the class started
        print("Open Application")

    @classmethod
    def tearDownClass(cls):  # Will execute after the class ends
        print("Close Application")

    def test_search(self):
        print("This is search test")

    def test_advancedsearch(self):
        print("This is advanced search")

    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is post paidRecharge test")


if __name__ == "__main__":
    unittest.main()
