import pytest

from square import pythagorean_triplets_brute_force

def test_pythagorean_zero():
    assert pythagorean_triplets_brute_force(0) == []


def test_pythagorean_invalid_type():
    with pytest.raises(TypeError):
        pythagorean_triplets_brute_force("a")