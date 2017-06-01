# Problem here: https://leetcode.com/problems/alien-dictionary/#/description
# Solution is to compare every consecutive pair of words to build up precedence graph and then topo-sort this
# graph to get a character order that makes sense.
# Time taken: 1 hr

from collections import defaultdict

def get_first_different_letter_idx(w1, w2):
    smaller_word_length = min(len(w1), len(w2))

    for i in range(smaller_word_length):
        if w1[i] != w2[i]:
            return i

    return -1

def build_precedence_graph(sorted_words):
    """Returns a tuple of (char_to_children, char_to_parents).
    """
    char_to_children = defaultdict(list)
    char_to_parents = defaultdict(list)
    for i in range(len(sorted_words) - 1):
        w1 = sorted_words[i]
        w2 = sorted_words[i + 1]
        first_different_letter_idx = get_first_different_letter_idx(w1, w2)

        # Create precedence link
        if first_different_letter_idx != -1:
            c1 = w1[first_different_letter_idx]
            c2 = w2[first_different_letter_idx]
            char_to_children[c1].append(c2)
            char_to_parents[c2].append(c1)

    return (char_to_children, char_to_parents)

def get_all_chars(words):
    cs = set()
    for w in words:
        cs |= set(w)
    return cs

def topological_sort(all_chars, char_to_children, char_to_parents):
    """Return a list of characters representing a topological sort of the provided graph. Will return [] if
    there is no valid topo-sort (i.e. there are cycles).
    """
    char_to_num_remaining_parents = {c: len(char_to_parents[c]) for c in all_chars}
    queue = [c for (c, num_parents) in char_to_num_remaining_parents.items() if num_parents == 0]

    topo_sort = []
    while len(queue) > 0:
        next_c = queue.pop()
        topo_sort.append(next_c)

        children = char_to_children[next_c]
        for child in children:
            char_to_num_remaining_parents[child] -= 1
            if char_to_num_remaining_parents[child] == 0:
                queue.append(child)

    # This will happen if there are cycles
    if any([num_parents > 0 for (c, num_parents) in char_to_num_remaining_parents.items()]):
        return []

    return topo_sort

def get_letter_order(sorted_words):
    # Build precedence graph
    (char_to_children, char_to_parents) = build_precedence_graph(sorted_words)
    all_chars = get_all_chars(sorted_words)
    sort_order = topological_sort(all_chars, char_to_children, char_to_parents)
    return "".join(sort_order)
