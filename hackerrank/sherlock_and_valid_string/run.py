from collections import defaultdict

def count_map(iterable):
    counts = defaultdict(lambda: 0)
    for x in iterable:
        counts[x] += 1
    return counts

def is_valid(s):
    char_counts = count_map(s)

    counts_of_counts = count_map(char_counts.values())

    if len(counts_of_counts.keys()) < 2:
        return True
    elif len(counts_of_counts.keys()) > 2:
        return False

    else:
        k1, k2  = counts_of_counts.keys()
        v1, v2 = [counts_of_counts[k] for k in [k1, k2]]

        # special case of just one
        if (k1 == 1 and v1 == 1) or (k2 == 1 and v2 == 1):
            return True

        # counts are one apart and there's only 1 of one count
        return abs(k1 - k2) == 1 and (v1 == 1 or v2 == 1)

s = input().strip()
result = is_valid(s)
if result:
    print('YES')
else:
    print('NO')
