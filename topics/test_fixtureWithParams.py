import pytest

@pytest.fixture()
def fixture_simple():
    return "Value from fixture_simple!"
@pytest.fixture()
def fixture_with_args(request, fixture_simple,arg1,arg2,arg3 ):
    print(request)
    print(fixture_simple)
    print(arg1)
    print(arg2)
    print(arg3)

@pytest.mark.parametrize("arg1, arg2, arg3", [(1,2,3)])
def test_01(fixture_with_args,arg1,arg2,arg3):
    pass
