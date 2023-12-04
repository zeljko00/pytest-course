import pytest
import os

@pytest.fixture()
def local_generic_fixture():
    print("Hello from local generic fixture!")
    yield
    print("Bye from local generic fixture!")
@pytest.fixture()
def setup01():
    return [1,2,3,4,5,6,7]

def test_withFixture(setup01):
    assert len(setup01)==7

data=[]
@pytest.fixture()
def setup02():
    # setup logic
    print()
    print("Setting everything up!")
    data=[x for x in range(100)]
    # returning data for tests
    yield data
    # clean up/teardown logic
    print()
    print("Cleaning up!")
    data.clear()

def test_oddNums(setup02):
    for x in setup02:
        assert x%2==1


@pytest.fixture()
def setup03():
    file=open("tmp.txt","w+")
    file.write("Hello Test!")
    file.flush()
    file.seek(0)
    yield file
    file.close()
    os.remove(file.name)

def test_readFile(setup03):
    assert setup03.readline()=="Hello Test!"

def test_withGlobalFixture(setup_global01):
    # accessing variable defined in pytest_configure func in conftest.py
    assert pytest.var=="pytest var"
    assert setup_global01=="Fixture from conftest.py file!"

testModuleVar="random"

def test_04(setup_global02):
    assert 1==1

def test_05(setup_factory):
    assert type(setup_factory("list"))==list
    assert type(setup_factory(""))==tuple

def test_06(setup_parameterized):
    assert setup_parameterized[0]<setup_parameterized[1]

@pytest.mark.scopedfix
def test_07(setup_function):
    pass

@pytest.mark.scopedfix
def test_08(setup_function):
    pass

@pytest.mark.scopedfix
def test_09(setup_module):
    pass

@pytest.mark.scopedfix
def test_10(setup_module):
    pass

def test_11(fixture_with_cmd_args):
    print(fixture_with_cmd_args)

