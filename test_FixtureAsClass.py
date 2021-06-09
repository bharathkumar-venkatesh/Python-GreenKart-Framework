import pytest


@pytest.mark.usefixtures("IamPreReq")
class FixtureAsClass:

    def test_New1(self):
        print("I need browser invocation")

    def test_Test2(self):
        print("I need browser invocation")

    def test_Test3(self):
        print("I need browser invocation")

    def test_Test4(self):
        print("I need browser invocation")

    @pytest.mark.skip
    def test_Test5(self):
        print("I need browser invocation")
