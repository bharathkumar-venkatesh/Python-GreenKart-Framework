import pytest


@pytest.mark.usefixtures("LoadData")
class TestExample2:

    def test_editProfile(self, LoadData):
        print(LoadData[0])
        print(LoadData[1])
        print(LoadData[2])