import pytest


@pytest.yield_fixture()
def setUp():
    print("Opening URL to signup")
    yield
    print("Closing browser after signup")


def test_signupByemail(setUp):
    print("this is signup by email test")


def test_signupByfacebook(setUp):
    print("this is signup by facebook test")

# Run all tests:
# C:\Users\Usuario\PycharmProjects\Selenium_with_Python\MyPack>pytest -v -s C:\Users\Usuario\PycharmProjects\Selenium_with_Python\MyPack


# Run Specifc test:
# C:\Users\Usuario\PycharmProjects\Selenium_with_Python\MyPack>pytest -v -s Test_SignUp.py

# Run specific test from a module:
# C:\Users\Usuario\PycharmProjects\Selenium_with_Python\MyPack>pytest -v -s Test_SignUp.py::test_signupByfacebook
