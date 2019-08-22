import pytest


@pytest.yield_fixture()
def setUp():
    print("Opening URL to Login")
    yield
    print("Closing browser after Login")


def test_loginByemail(setUp):
    print("this is login by email test")


def test_loginByfacebook(setUp):
    print("this is login by facebook test")
