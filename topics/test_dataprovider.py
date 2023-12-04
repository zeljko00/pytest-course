from topics.utils.util import read_data
import pytest

@pytest.mark.parametrize("id, firstname, lastname, city", read_data())
def test_data_provider(id, firstname, lastname, city):
    print("id={} , name={} {} , city={}".format(id, firstname, lastname, city))

