import pytest


@pytest.fixture()
def IamPreReq():
    print("Browser invoked")
    yield
    print("Closing the browser")


@pytest.fixture()
def LoadData():
    print("Creating Data")
    return ["Bharath", "Barry", "junglebeats.wildlife.com"]


@pytest.fixture(params=[("chrome", "Bharath"), ("firefox", "Barry"), ("IE", "KKR")])
def MultiData(request):
    return request.param
