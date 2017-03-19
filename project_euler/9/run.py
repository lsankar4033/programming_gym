from itertools import combinations
from math import sqrt

s = set([x ** 2 for x in range(1, 1000)])
p = [(sqrt(a), sqrt(b), sqrt(a + b)) for (a, b) in combinations(s, 2) if (a + b)
     in s]
f = [a * b * c for (a, b, c) in p if (a + b + c) == 1000.0]

print f
