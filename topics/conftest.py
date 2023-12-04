import pytest

def pytest_configure():
    pytest.var="pytest var"

@pytest.fixture()
def generic_fixture():
    print("\n Hello from generic fixture!")
    yield
    print("\n Bye from generic fixture!")
@pytest.fixture()
def setup_global01():
    print("Hello from fixture on conftest.py!")
    yield "Fixture from conftest.py file!"
    print("Bye from fixture on conftest.py!")

@pytest.fixture()
def setup_global02(request):
    print("\n Fixture setup_global02!")
    print("\n Fixture scope: "+request.scope+"!")
    print("\n Test func name: "+request.function.__name__+"!")
    print("\n Test module name: "+request.module.__name__+"!")
    print("\n Variable from test function module: "+getattr(request.module,"testModuleVar"))

@pytest.fixture()
def setup_factory():
    def generator(collection):
        if collection=="list":
            return []
        else:
            return ()
    return generator

@pytest.fixture(params=[(1,2),(2,3),(3,4),(5,4),(5,6)],ids=["fp1","fp2","fp3","fp4","fp5"])
def setup_parameterized(request):
    print("\n Setting everything up!")
    yield request.param
    print("\n Cleaning up!")


@pytest.fixture(scope="function")
def setup_function():
    print("\n Function fixture setting up!")
    yield
    print("\n Function fixture cleaning up!")

@pytest.fixture(scope="module")
def setup_module():
    print("\n Module fixture setting up!")
    yield
    print("\n Module fixture cleaning up!")


# initialization hook for accessing test arguments passed via cmd
def pytest_addoption(parser):
    parser.addoption("--arg",default="default arg value")

@pytest.fixture()
def fixture_with_cmd_args(pytestconfig):
    return pytestconfig.getoption("--arg")

from topics.utils import ConfigReader
@pytest.fixture(scope="module")
def setup_config():
    return ConfigReader.ConfigReader("config.ini")