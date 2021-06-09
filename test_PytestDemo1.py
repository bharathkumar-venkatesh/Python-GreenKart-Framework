# Any pyTest file should always start with the name test followed by underscore. Ex: test_Demo
# or end with _test. Ex: Demo_test
# pyTest method names should always start with test keyword. Ex: test_method name
# Any code should be wrapped inside a method
# In Pytest, we cannot have same Test name for 2 methods. If there are 2 with same names, it is over ridden
import pytest


@pytest.mark.smoke
def test_PytestDemo():
    print("I am running my first pytest code")


def test_PytestDemo2():
    print("Its my second test and i am running it on the console")


def test_New3():
    print("Trying to run selected tests")


def test_PytestDemo4():
    print("KKR will win IPL")
