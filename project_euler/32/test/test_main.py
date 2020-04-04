from pe.main import *


def test_pandigitals():
    assert pandigitals(1) == [[1]]
    assert pandigitals(2) == [[1, 2], [2, 1]]
    assert pandigitals(3) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


def test_digits_to_num():
    assert digits_to_num([1, 3, 2]) == 132
    assert digits_to_num([5, 3, 7]) == 537


def test_is_valid_mult():
    assert not is_valid_mult([1, 2, 3], 0, 1)
    assert is_valid_mult([1, 2, 2], 0, 1)

    assert is_valid_mult([2, 3, 2, 4, 6], 1, 2)
    assert not is_valid_mult([2, 3, 2, 4, 6], 1, 3)

    assert is_valid_mult([3, 9, 1, 8, 6, 7, 2, 5, 4], 1, 4)
