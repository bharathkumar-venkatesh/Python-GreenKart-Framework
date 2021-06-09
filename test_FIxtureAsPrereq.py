import pytest


def test_Test1(IamPreReq):
    print("I need browser invocation")


def test_Test2(IamPreReq):
    print("I need browser invocation")


def test_Test3(IamPreReq):
    print("I need browser invocation")


def test_Test4(IamPreReq):
    print("I need browser invocation")


@pytest.mark.skip
def test_Test5(IamPreReq):
    print("I need browser invocation")
