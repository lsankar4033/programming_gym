from collections import defaultdict


def is_right(a, b, c):
    a2 = a * a
    b2 = b * b
    c2 = c * c

    return a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2


if __name__ == '__main__':
    perims = defaultdict(lambda: 0)
    for a in range(1000):
        for b in range(a, 1000):

            if (a + b) < 1000:
                for c in range(b - a + 1, b + a - 1):
                    perim = a + b + c
                    if perim <= 1000 and is_right(a, b, c):
                        print(f"({a}, {b}, {c}) ; {perim}")
                        perims[perim] += 1

    print(f"{perims}")
