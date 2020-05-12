import pytest

def perimRect(length,width):
   """
   Compute perimiter of rectangle
   """
   return 2 * length + 2* width # stub  @@@ replace this stub with the correct code @@@

def test_perimRect_1():
   assert perimRect(4,5)==18

def test_perimRect_2():
   assert perimRect(7,3)==20

def test_perimRect_3():
   assert perimRect(2.1,4.3)==pytest.approx(12.8)

def test_perimRect_4():
   assert perimRect(5,5)==20


def areaRect(length, width):
    return length * width

def test_areaRect_1():
   assert areaRect(3,4)==12

def test_areaRect_2():
   assert areaRect(0.5,0.4)==pytest.approx(0.2)

def test_areaRect_3():
    assert areaRect(1, 1) == 1


def isString(x):
   """
   returns True if argument is of type str, otherwise False
   """
   
   return ( type(x) == str )

def test_isString_1():
   assert isString("UCSB")

def test_isString_2():
   assert not isString(42)

def test_isString_3():
   assert not isString(["UCSB"])

def test_isString_4():
   assert isString('78')

def test_isString_5():
   assert not isString(78)


def isNumber(x):
    return type(x) == int or type(x) == float

def test_isNumber_1():
    assert isNumber(1)

def test_isNumber_2():
    assert not isNumber('k')

def test_isNumber_3():
    assert not isNumber(['k'])

def test_isNumber_4():
    assert isNumber(1.0)

def test_isNumber_5():
    assert not isNumber((1,))
