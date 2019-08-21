import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignUpTest

from Package2.PC_PaymentTest import PaymentTest
from Package2.PC_PaymentReturnTest import PaymentReturnTest

# Get all tests from LoginTest, SignUpTest, PaymentTest and PaymentReturnsTest (with TestLoader().loadTestsFromTestCase)

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

# CREATING TEST SUITES
sanityTestSuite = unittest.TestSuite([tc1, tc2])  # Sanity Test Suite
functionalTestSuite = unittest.TestSuite([tc3, tc4])  # Functional Test Suite
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])  # Master Test Suite

unittest.TextTestRunner(verbosity=2).run(masterTestSuite)
