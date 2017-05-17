from collections import defaultdict
from itertools import combinations

def build_char_map(s):
    ret = defaultdict(list)
    for (i, c) in enumerate(s):
        ret[c].append(i)

    return ret

def pair_is_valid(c1, c2):
    # Add these conditions to loop as well
    if len(c1) == 0 and len(c2) > 1:
        return False
    if len(c2) == 0 and len(c1) > 1:
        return False
    if len(c1) == 0 and len(c2) == 0:
        return True

    prev_was_1 = False
    if min(c1[0], c2[0]) == c1[0]:
        prev_was_1 = True
        c1 = c1[1:]
    else:
        c2 = c2[1:]

    while len(c1) >= 0 and len(c2) >= 0:
        if len(c1) == 0:
            return len(c2) < 2
        if len(c2) == 0:
            return len(c1) < 2

        m = min(c1[0], c2[0])
        if m == c1[0] and prev_was_1:
            return False
        elif m == c2[0] and not prev_was_1:
            return False

        if m == c1[0]:
            prev_was_1 = True
            c1 = c1[1:]
        else:
            prev_was_1 = False
            c2 = c2[1:]

    return True

def find_longest(c_map):
    longest = 0
    for (c1, c2) in combinations(c_map.keys(), 2):

        if pair_is_valid(c_map[c1], c_map[c2]):
            length = len(c_map[c1]) + len(c_map[c2])
            if length > longest:
                longest = length

    return longest

_ = input()
s = input()

c_map = build_char_map(s)
print(find_longest(c_map))
