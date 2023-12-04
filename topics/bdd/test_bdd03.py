import pytest_bdd
import pathlib
import pytest

featureFileName="f02.feature"
featureFileDir="features"

featureFile=pathlib.Path(__file__).resolve().parent.joinpath(featureFileDir).joinpath(featureFileName)

pytest_bdd.scenarios(featureFile)

@pytest_bdd.given(pytest_bdd.p"dividend is {a:d}",target_fixture="dividend")
def setup_dividend():
    return a

