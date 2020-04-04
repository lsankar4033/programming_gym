from pe.main import *


def test_score():
    assert score('SKY') == 55
    assert score('SKZ') == 56


def test_tri_gen():
    tri_g = tri_gen()

    assert next(tri_g) == 1
    assert next(tri_g) == 3
    assert next(tri_g) == 6
    assert next(tri_g) == 10
    assert next(tri_g) == 15
    assert next(tri_g) == 21
    assert next(tri_g) == 28
