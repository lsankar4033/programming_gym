from itertools import count, chain
from math import sqrt


def num_divisors(i):
    div = ([x, i / x] for x in range(1, int(sqrt(i)) + 1) if i % x == 0)
    return len(set(chain(*div)))

tri = (sum(xrange(i + 1)) for i in count(1))
print next(i for i in tri if num_divisors(i) > 500)
