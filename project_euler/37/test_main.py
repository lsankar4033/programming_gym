from src.main import truncations


def test_truncations():
    assert truncations(1) == set([1])

    assert truncations(12) == set([1, 2, 12])

    assert truncations(3797) == set([3797, 797, 97, 7, 379, 37, 3])
