import pytest

@pytest.mark.parametrize(argnames="value", argvalues=range(10))
def test_back(value):
    # assert value%11 != 0
    pass