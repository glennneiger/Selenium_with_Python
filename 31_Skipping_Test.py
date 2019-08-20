import unittest


class Apptesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("This is search test")

    @unittest.skip("Skipping test method because is not ready")
    def test_advancedsearch(self):
        print("This is advanced search")

    @unittest.skipIf(1 == 1, "ONE IS EQUAL TO ONE")
    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is post paidRecharge test")

    def test_loginbygmail(self):
        print("This is login by email")

    def test_loginbytwitter(self):
        print("This is login by twitter")


if __name__ == "__main__":
    unittest.main()
