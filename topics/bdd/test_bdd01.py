import pytest_bdd
import pathlib
import pytest

featureFileName="f01.feature"
featureFileDir="features"

featureFile=pathlib.Path(__file__).resolve().parent.joinpath(featureFileDir).joinpath(featureFileName)

# used only for creating global var accessible from all pytest tests
def pytest_confgure():
    pytest.acc_balance=0

# this will execute all scenarion from specified while, in case they have defined all steps
pytest_bdd.scenarios(featureFile)

# this function is called after execution of test scenario, but also initiates scenario test execution
# @pytest_bdd.scenario(featureFile,"Money withdrawal")
# def test_withdrawal():
#     print("End of bank transaction!")
#     pass

@pytest_bdd.given("start of background actions")
def start_background():
    print("Starting background actions!")

@pytest_bdd.given("end of background actions")
def end_background():
    print("Ending background actions!")

@pytest_bdd.given("account balance is 100$")
def set_balance():
    pytest.acc_balance=100

@pytest_bdd.when("account owner withdraws 70$")
def withdraw_money():
    pytest.acc_balance-=70

@pytest_bdd.then("account balance is 30$")
def check_balance():
    assert pytest.acc_balance==30

# @pytest_bdd.scenario(featureFile,"Set manipulation")
# def test_set():
#     print("End of set manipulation test!")

@pytest_bdd.given("set has 3 elements", target_fixture="set")
def setup_set():
    return {"apple","orange","banana"}

@pytest_bdd.when("remove random element")
def remove_element(set):
    set.pop()

@pytest_bdd.then("set has 2 elements now")
def check_set(set):
    assert len(set)==2




