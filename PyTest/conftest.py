import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")


@pytest.fixture()
def dataLoad():
    print("user profile/data is being creadted")
    return ["richa", "tyagi", "richatyagiacadmeny.com"]



@pytest.fixture(params=[("chrome","Richa","shetty"),("Firefox","Riyaa"),("IE","SS")])
def crossBrowser(request):
   return request.param