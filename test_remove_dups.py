import pytest
from main import remove_dups

@pytest.mark.parametrize("list_input, output", [
    (["red", "blue", "red"], ["blue", "red"]),
    ([], False),
    ("red", False),
])
def test_remove_dups(list_input, output):
    assert remove_dups(list_input) == output