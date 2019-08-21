import unittest


class Test(unittest.TestCase):
    def testName(self):
        list = ["python", "selenium", "java"]
        # self.assertIn("python", list) #passed
        # self.assertIn("ruby", list) #failed

        self.assertNotIn("python", list)  # failed
        self.assertNotIn("ruby", list)  # pass


if __name__ == '__main__':
    unittest.main()

# Note: these kinds of assertions is very useful to verify presence of a value in a list, tuple, set and dictionary.
