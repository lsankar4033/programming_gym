from pe.main import *


def test_same_value_g():
    def g1():
        for i in range(10):
            yield i

        yield 11
        yield 13
        yield 22

        while True:
            yield 50

    def g2():
        yield 1
        yield 3
        yield 8
        for i in range(10, 30):
            yield i

        while True:
            yield 50

    sg = same_value_g(g1(), g2())

    print("Starting generation")
    assert next(sg) == 1
    assert next(sg) == 3
    assert next(sg) == 8

    assert next(sg) == 11
    assert next(sg) == 13
    assert next(sg) == 22

    assert next(sg) == 50
    assert next(sg) == 50
