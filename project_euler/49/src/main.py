from collections import defaultdict
from math import sqrt

from typing import List, Set


def perm_sets(start=1000, end=10000):
    perm_sets = defaultdict(set)
    for n in range(start, end):
        composite = False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                composite = True
                break

        if not composite:
            key = ''.join(sorted(str(n)))
            perm_sets[key].add(n)

    return perm_sets


def arith_seqs_3(ns: Set[int]):
    sorted_ns = sorted(ns)

    seqs = []
    for i in range(len(sorted_ns)):
        for j in range(i + 1, len(sorted_ns)):
            a1 = sorted_ns[i]
            a2 = sorted_ns[j]
            a3 = a2 + (a2 - a1)

            if a3 in ns:
                seqs.append([a1, a2, a3])

    return seqs


if __name__ == '__main__':
    print('Building perm sets')
    ps = perm_sets()

    all_seqs = []
    for _, ns in ps.items():
        seqs = arith_seqs_3(ns)
        if len(seqs) > 0:
            all_seqs += seqs

    for seq in all_seqs:
        print(''.join(map(str, seq)))
