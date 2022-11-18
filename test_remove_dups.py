import pytest
from main import remove_dups

@pytest.mark.parametrize("list_test, output", [
    (["red", "red", "blue"], ["red","blue"]),
    ([], False),
    ("red", False),
    (9, False),
    ({"red": 1}, False),
    (["red", "red", "blue", 9], False),
    (["red", "red", "blue", bool], False),
    (["red", "red", "blue", ["red","blue"]], False),
    (["red", "red", "blue", {"red": 1}], False)
])
def test_remove_dups(list_test, output):
    assert remove_dups(list_test) == output