# Problem here: https://leetcode.com/problems/word-squares/#/description
# Time taken: 65 mins

def build_trie(words):
    """Trie is a nested map where word ends indicated with empty maps.

    Problem statement asserts no duplicates so we don't keep track of word counts here.
    """
    trie = {}

    for word in words:
        cur_level = trie
        for char in word:
            if char not in cur_level:
                cur_level[char] = {}

            cur_level = cur_level[char]

    return trie

def enumerate_words_from_trie(trie):
    if len(trie) == 0:
        return ['']

    all_words = []
    for c in trie:
        subwords = enumerate_words_from_trie(trie[c])
        all_words.extend([c + w for w in subwords])

    return all_words

def get_words_with_prefix(prefix, trie):
    cur_level = trie
    for c in prefix:
        if c not in cur_level:
            return []
        else:
            cur_level = cur_level[c]

    valid_suffixes = enumerate_words_from_trie(cur_level)
    return ["".join(prefix) + suffix for suffix in valid_suffixes]

def get_word_squares_recur(words_so_far, trie, word_squares):
    constraint_idx = len(words_so_far)
    if constraint_idx > len(words_so_far[0]) - 1:
        word_squares.append(words_so_far)

    else:
        prefix = [w[constraint_idx] for w in words_so_far]
        words_with_prefix = get_words_with_prefix(prefix, trie)

        for word in words_with_prefix:
            get_word_squares_recur(words_so_far + [word], trie, word_squares)

def get_word_squares(words):
    trie = build_trie(words)

    # NOTE: this could have been handled in the recursion logic above
    word_squares = []
    for word in words:
        get_word_squares_recur([word], trie, word_squares)

    return word_squares
