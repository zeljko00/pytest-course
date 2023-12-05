import pytest_bdd
import pathlib
import pytest

featureFileName="f02.feature"
featureFileDir="features"

featureFile=pathlib.Path(__file__).resolve().parent.joinpath(featureFileDir).joinpath(featureFileName)

pytest_bdd.scenarios(featureFile)

@pytest_bdd.given(pytest_bdd.parsers.parse("dividend is {a:d}"),target_fixture="dividend")
def setup_dividend(a):
    return a

@pytest_bdd.when(pytest_bdd.parsers.parse("divide by {b:d}"),target_fixture="result")
def divide(b,dividend):
    print(str(dividend)+" / "+str(b))
    return dividend/b

@pytest_bdd.then(pytest_bdd.parsers.parse("result is {r:d}"))
def check_result(r,result):
    print(str(r)+" == "+str(result))
    assert r==result

@pytest_bdd.then("if divide by 0",target_fixture="result2")
def divide_by_zero(dividend):
    print(str(dividend)+" / 0")
    try:
        result=dividend/0
        return result
    except:
        return "NaN"

@pytest_bdd.then("result is NaN")
def check_nan(result2):
    print("NaN == "+str(result2))
    assert "NaN"==result2