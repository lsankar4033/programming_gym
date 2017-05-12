# Problem here: https://www.hackerrank.com/challenges/string-function-calculation

import sys
from collections import defaultdict

# TODO: this works but is way too slow... Rather than doing linear DP, maybe I can do something that searches
# through the space in log time or something?

# Hint is that suffix trees/suffix arrays/LCP arrays may be useful. How?
# - substring search is very quick on a suffix tree because every substring is a prefix of a suffix, so we have
# to do at most |s| comparisons (where s is substring)
# - suffix array groups similar substrings together... this seems useful
# - suffix array lexicographic ordering means that finding all existences of a single substring takes two
# binary searches = O(mlogn)
# - LCP array is array of longest common prefixes of adjacent members of suffix array. can supplement suffix
# array search of all existences of a single substring to O(m+logn)

# There's a lot to digest here. I'll come back to this one.

# NOTE - this method is just copied around in all hackerrank modules
def get_str_from_stdin():
    return sys.stdin.readline().strip()

def compute_max_s(t):
    print("Computing f(S) for substrings of length 1")
    sub_map = defaultdict(list)
    for (i, c) in enumerate(t):
        sub_map[c].append(i)
    cur_max = max((len(vs) for vs in sub_map.items()))
    cur_max = max(cur_max, len(t)) # Compare with whole string substring
    print("Max so far (including whole string): {}".format(cur_max))

    for sub_len in range(2, len(t)):
        print("Max so far: {}".format(cur_max))
        print("Computing f(S) for substrings of length {}".format(sub_len))

        new_sub_map = defaultdict(list)
        for start in range(len(t) + 1 - sub_len):
            new_sub = t[start:start + sub_len]
            if new_sub in new_sub_map:
                continue

            child_sub = new_sub[:-1]
            count = 0
            for child_start in sub_map[child_sub]:
                if child_start + sub_len <= len(t) and t[child_start + sub_len - 1] == new_sub[-1]:
                    count += 1
                    new_sub_map[new_sub].append(child_start)

            cur_max = max(cur_max, count * sub_len)

        sub_map = new_sub_map

    return cur_max

if __name__ == "__main__":
    t = get_str_from_stdin()
    print(compute_max_s(t))
