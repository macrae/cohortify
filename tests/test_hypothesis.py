from hypothesis import given
from hypothesis.strategies import dictionaries, integers


@given(integers())
def test_integers(i):
    print(i)
    assert isinstance(i, int)


@given(dictionaries(integers(), integers()))
def test_dicts(d):
    print(d)
    assert isinstance(d, dict)
