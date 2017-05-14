# Problem here: https://www.hackerrank.com/challenges/sherlock-and-anagrams
# Iterate through all substrings (n^2) time and for each length, group substrings by char maps
import math

from collections import defaultdict

# NOTE: not to be mutated!
class hashabledict(dict):
    def __key(self):
        return tuple((k,self[k]) for k in sorted(self))
    def __hash__(self):
        return hash(self.__key())
    def __eq__(self, other):
        return self.__key() == other.__key()

def _get_grouping_key(s):
    grouping_key_dict = defaultdict(lambda: 0)
    for c in s:
        grouping_key_dict[c] += 1

    return hashabledict(grouping_key_dict)

def comb(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)

def _get_num_pairs_for_length(s, length):
    anagram_groupings = defaultdict(lambda: 0)
    for start in range(len(s) - length + 1):
        sub = s[start:start + length]
        anagram_groupings[_get_grouping_key(sub)] += 1

    num_pairs = 0
    for group_size in anagram_groupings.values():
        if group_size > 1:
            num_pairs += comb(group_size, 2)

    return num_pairs

def get_num_pairs(s):
    num_pairs = 0
    for length in range(1, len(s)):
        num_pairs += _get_num_pairs_for_length(s, length)

    return int(num_pairs)

num_cases = int(input().strip())

for _ in range(num_cases):
    print(get_num_pairs(input().strip()))
