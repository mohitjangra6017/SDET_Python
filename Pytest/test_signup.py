import pytest


def test_1():
    a = 3
    b = 4
    assert a + 1 == b, "test failed"
    assert a != b, "not equal"

def test_2():
    name = "mohit"
    assert name.upper()== "MOHIT"

def test_3():
    assert True

def test_4():
    assert False

def test_5():
    assert "mohitjangra" == "MOHITJANGRA"
