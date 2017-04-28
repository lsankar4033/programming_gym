# Problem here: https://projecteuler.net/problem=98

import math

from collections import defaultdict
from itertools import chain, combinations, groupby, product

# NOTE these are assumed to be immutable!
class hashabledict(dict):
    def __key(self):
        return tuple((k,self[k]) for k in sorted(self))
    def __hash__(self):
        return hash(self.__key())
    def __eq__(self, other):
        return self.__key() == other.__key()

words_file = "words.txt"

def words_from_file():
    words = []
    with open(words_file, "r") as f:
        words = f.readline().strip().replace("\"", "").split(",")
        # Only words with unique letters
        words = list(filter(lambda w: len(set(w)) == len(w), words))

    return words

def get_word_key(word):
    return "".join(sorted(word))

# returns a list of sets where each set contains mutual anagrams
def collect_anagrams(words):
    word_dict_to_words = defaultdict(set)
    for k, v in groupby(words, get_word_key):
        word_dict_to_words[k] |= set(v)

    # Remove all 1 length anagram groupings (single words)
    ret = {}
    for k, v in word_dict_to_words.items():
        if len(v) > 1:
            ret[k] = v

    return ret.values()

# use this along with collect_anagrams to build the anagrams of squares
def get_squares(num_digits):
    lower_bound = math.ceil( math.sqrt( pow(10, num_digits - 1) - 1 ) )
    upper_bound = math.ceil( math.sqrt( pow(10, num_digits) ) )
    return (i * i for i in range(lower_bound, upper_bound))

def get_permutations(s1, s2):
    index_lists = [[i for (i,x) in enumerate(s1) if x == c] for c in s2]

    def get_all_index_lists(cur_partial, next_i):
        if next_i > len(index_lists) - 1:
            return [cur_partial]
        ret = []
        for i in index_lists[next_i]:
            ret += get_all_index_lists(cur_partial + (i,), next_i + 1)
        return ret

    return get_all_index_lists((), 0)

def perm_applies(perm, s1, s2):
    test_tmp = []
    for i in perm:
        test_tmp.append(s1[i])

    return "".join(test_tmp) == s2

# Makes sure that the given permutation doesn't map a different letters to multiple digits (in the squares) in
# at least one of the possible arrangements of words and squares
def is_valid_perm(perm, w1, w2, s1, s2):
    # The below code is cumbersome...
    possible_w_orders = []
    for (i, j) in [[w1, w2], [w2, w1]]:
        if perm_applies(perm, i, j):
            possible_w_orders.append([i,j])

    possible_s_orders = []
    for (i, j) in [[s1, s2], [s2, s1]]:
        if perm_applies(perm, i, j):
            possible_s_orders.append([i,j])

    for ((w1, _), (s1, _)) in product(possible_w_orders, possible_s_orders):
        # If there are multiple letters being mapped to a single digit, return false
        digit_to_letters = defaultdict(set)
        for i in range(len(w1)):
            if s1[i] in digit_to_letters and s1[i] != set([w1[i]]):
                return False

            digit_to_letters[s1[i]].add(w1[i])

    return True

def get_max_anagram_square(word_anagrams, str_square_anagrams):
    word_anagram_pairs = chain.from_iterable((combinations(anagrams, 2) for anagrams in word_anagrams))
    str_square_anagram_pairs = chain.from_iterable((combinations(anagrams, 2) for anagrams in str_square_anagrams))

    max_anagram_square = None
    for ((w1, w2), (s1, s2)) in product(word_anagram_pairs, str_square_anagram_pairs):
        word_permutations = set(get_permutations(w1, w2))
        square_permutations = set(get_permutations(s1, s2)) | set(get_permutations(s2, s1))

        common_permutations = square_permutations & word_permutations
        valid_permutations = filter(lambda p: is_valid_perm(p, w1, w2, s1, s2), common_permutations)
        if len(list(valid_permutations)) > 0:
            max_square = max(int(s1), int(s2))
            if max_anagram_square is None or max_square > max_anagram_square:
                max_anagram_square = max_square

    return max_anagram_square

if __name__ == "__main__":
    all_words = words_from_file()
    anagrams = collect_anagrams(all_words)

    len_to_anagram_sets = defaultdict(list)
    for anagram_set in anagrams:
        len_to_anagram_sets[len(list(anagram_set)[0])].append(anagram_set)

    # Now, for each anagram length in the above set, generate the set of anagrammic squares at that length and
    # try all of them!
    for length in sorted(len_to_anagram_sets, reverse=True):
        print("Checking squares of length {}".format(length))

        word_anagrams = len_to_anagram_sets[length]

        # get square anagrams
        all_squares = get_squares(length)
        str_squares = (str(s) for s in all_squares)
        str_square_anagrams = collect_anagrams(str_squares)

        # find max anagram square (function of square_anagrams and word_anagram)
        # return immediately if we find one because we're going through squares in reverse length order
        max_anagram_square = get_max_anagram_square(word_anagrams, str_square_anagrams)
        if max_anagram_square is not None:
            print(max_anagram_square)
            break

    print("Done.")
