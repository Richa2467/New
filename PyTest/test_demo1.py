#Any python file should start with test_ or end with _test
#pytest method names should start with test
#every line should be under any function
#Any code should be wrraped in methods
#Method name should have sance
# -k stands for methods name execution
# -s stands for output
# -v stands for more info metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run with -m pytest -m smoke -v -s
# you can skip the test using @pytest.mark.skip
# Fixtures are used as setup and tear down methods for test cases- conftest file to generalize fixture make it available to all test cases.


import pytest



@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg= "Hii"    #operations
    assert msg == "Hlo", "Failed due to string don't match"

def test_SecondCreditCard():
    a=4
    b=6
    assert a+2 == 6, "Addition do not match"


@pytest.fixture()
def setup():
    print("I will be executed first")


def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo  method")