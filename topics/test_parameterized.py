import pytest
import functools
import os
@pytest.mark.parametrize("arg",[1,2,3,None])
def test_param01(arg):
    assert arg is not None

data1=[(1,1),(2,2),(2,None)]
@pytest.mark.parametrize("arg1, arg2",data1)
def test_param02(arg1,arg2):
    assert (arg1 is not None) and (arg2 is not None)

def calc_cum(elements):
    return functools.reduce(lambda  a,b: a+b,elements,0)
    # return sum(elements)

data2=[([1,2,3,4],10),([5,6,7,8],26),([9,10,11,12],33)]
@pytest.mark.parametrize("data, sum",data2)
def test_param03(data, sum):
    assert calc_cum(data)==sum


