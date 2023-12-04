import pytest

@pytest.mark.suit1
def test_pass():
    print("Successful test!")
    assert 1==1

@pytest.mark.suit1
def test_fail():
    print("Failure!")
    assert 1==2, "Failed on purpose!"

class TestClass:
    def test_m1(self):
        assert "b" in "An apple","Success!"


def test_exc1():
    with pytest.raises(Exception) as exc:
        assert 1==1
def test_exc2():
    with pytest.raises(Exception) as exc:
        1/0
def test_exc3():
    with pytest.raises(Exception) as exc:
        raise  Exception("Custom exception!")
    assert str(exc.value)=="Value Error"
def test_exc4():
    with pytest.raises(Exception) as exc:
        raise  Exception("Custom exception!")
    assert str(exc.value)=="Custom exception!"
