import pytest_bdd
import pathlib
import pytest

# featureFileName="f03.feature"
featureFileName="f04_parametrized.feature"
featureFileDir="features"

featureFile=pathlib.Path(__file__).resolve().parent.joinpath(featureFileDir).joinpath(featureFileName)

pytest_bdd.scenarios(featureFile)

@pytest_bdd.given(pytest_bdd.parsers.parse("dividend is {a:d}"),target_fixture="data")
def setup_dividend(a):
    return a

@pytest_bdd.when(pytest_bdd.parsers.parse("divide by {b:d}"),target_fixture="data")
def divide(b,data):
    print(str(data)+" / "+str(b))
    return data/b

@pytest_bdd.then(pytest_bdd.parsers.parse("result is {r:d}"))
def check_result(r,data):
    print(str(r)+" == "+str(data))
    assert r==data