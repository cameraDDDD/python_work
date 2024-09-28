from practice11_3 import Employor
import pytest
@pytest.fixture
def e1():
    e1=Employor("K","H",5000)
    return e1


def test_give_default_raise(e1):
    #e1=Employor("k","h",5000)
    e1.give_raise(10)
    assert e1.salary==5010
def test_give_custom_raise(e1):
    #e1=Employor("k","h",5000)
    e1.give_raise()
    assert e1.salary==10000