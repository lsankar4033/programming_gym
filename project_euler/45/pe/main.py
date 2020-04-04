def tri_g():
    n = 1
    while True:
        yield n * (n + 1) / 2
        n += 1


def pent_g():
    n = 1
    while True:
        yield n * ((3 * n) - 1) / 2
        n += 1


def hex_g():
    n = 1
    while True:
        yield n * ((2 * n) - 1)
        n += 1


def same_value_g(g1, g2):
    c1 = next(g1)
    c2 = next(g2)

    while True:
        if c1 == c2:
            yield c1
            c1 = next(g1)
        elif c1 < c2:
            while c1 < c2:
                c1 = next(g1)
        else:
            while c2 < c1:
                c2 = next(g2)


if __name__ == '__main__':
    t = tri_g()
    p = pent_g()
    h = hex_g()

    tp_g = same_value_g(t, p)
    tph_g = same_value_g(tp_g, h)

    print(f"{next(tph_g)}")
    print(f"{next(tph_g)}")
    print(f"{next(tph_g)}")
