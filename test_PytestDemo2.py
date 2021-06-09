import pytest


@pytest.mark.skip
def test_AssertNew():
    msg = "Hello"
    assert msg == "Hi", "The test failed"


@pytest.mark.smoke
@pytest.mark.xfail
def test_PytestDemo5():
    a = 4
    b = 6
    assert a == b, "The test is not working fine"


@pytest.fixture()
def fixtureMethod():
    print("I am a fixture and I am prerequisite for the next test case")
    yield
    print("I am executed after the completion of Test execution")


def test_FixtureDemo(fixtureMethod):
    print("I am using the fixture and the the perquisites")
