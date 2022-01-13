import pytest


#
@pytest.fixture()
def setup():
    print("before")
    yield
    print("after")


def test1(setup):
    print("Test1")


#

def test2(setup):
    print("Test2")

#
# def test_m11():
#     name = "selenium"
#     assert name.upper() == "SELENIUM"
#     print("success")
