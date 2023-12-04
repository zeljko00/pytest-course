import pytest_bdd
import pathlib
import pytest

featureFileName="f01.feature"
featureFileDir="features"

featureFile=pathlib.Path(__file__).resolve().parent.joinpath(featureFileDir).joinpath(featureFileName)


@pytest.fixture()
def setup_setdata():
    return {"apple","orange","banana"}

@pytest_bdd.scenario(featureFile,"Set manipulation")
def test_set_withFixture(setup_setdata):
    print("End of set manipulation test!")

@pytest_bdd.given("set has 3 elements", target_fixture="set")
def setup_set(setup_setdata):
    return setup_setdata

@pytest_bdd.when("remove random element")
def remove_element(set):
    set.pop()

@pytest_bdd.then("Then: set has 2 elements now")
def check_set(set):
    assert len(set)==2




