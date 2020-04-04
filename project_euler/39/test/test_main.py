from pe.main import *


def test_is_right():
    assert is_right(3, 4, 5)
    assert is_right(4, 5, 3)
    assert is_right(5, 3, 4)

    assert is_right(51, 45, 24)

    assert not is_right(51, 45, 25)
