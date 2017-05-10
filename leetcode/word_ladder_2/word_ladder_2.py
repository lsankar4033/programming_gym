# Problem here: https://leetcode.com/problems/word-ladder-ii/#/description
# Solution is to build an undirected graph of words to each word to words 1 away and then do a 2-way BFS from
# start/end to find all shortest paths.

# TODO - time limit exceeded...

from itertools import chain, combinations, product
from collections import defaultdict

def _words_are_adjacent(w1, w2):
    assert len(w1) == len(w2), "Found two words in word list of different length: {}, {}".format(w1, w2)

    num_different = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            num_different += 1

    return num_different == 1

def _build_adjacency_map(begin_word, word_list):
    adj_map = defaultdict(set)
    word_list = word_list + [begin_word]
    for (w1, w2) in combinations(word_list, 2):
        if _words_are_adjacent(w1, w2):
            adj_map[w1].add(w2)
            adj_map[w2].add(w1)

    return adj_map

def _get_new_paths(adj_map, paths, visited):
    return list(chain.from_iterable(((path + [neighbor]
                                      for neighbor in adj_map[path[-1]] if neighbor not in visited)
                                     for path in paths)))

def _get_valid_ladders(paths_1, paths_2):
    return [p1 + list(reversed(p2))[1:]
            for (p1, p2) in product(paths_1, paths_2) if p1[-1] == p2[-1]]

def _unique_lists(lists):
    return [list(x) for x in set(tuple(y) for y in lists)]

def _find_ladders(adj_map, begin_word, end_word):
    visited_1 = set()
    visited_2 = set()
    paths_1 = [[begin_word]]
    paths_2 = [[end_word]]

    while len(paths_1) > 0 and len(paths_2) > 0:
        new_paths_1 = _get_new_paths(adj_map, paths_1, visited_1)
        new_paths_2 = _get_new_paths(adj_map, paths_2, visited_2)

        # first check case where either frontier collided with other set of paths
        shortest_paths = []
        shortest_paths += _get_valid_ladders(new_paths_1, paths_2)
        shortest_paths += _get_valid_ladders(paths_1, new_paths_2)
        if len(shortest_paths) > 0:
            return _unique_lists(shortest_paths)

        # next check case of frontiers colliding
        shortest_paths = _get_valid_ladders(new_paths_1, new_paths_2)
        if len(shortest_paths) > 0:
            return _unique_lists(shortest_paths)

        # finally, reset paths and add ends of all paths to visited
        visited_1 |= set([p[-1] for p in new_paths_1])
        visited_2 |= set([p[-1] for p in new_paths_2])
        paths_1 = new_paths_1
        paths_2 = new_paths_2

    return []

class Solution(object):
    # NOTE template uses camel case, but I use underscore case
    def findLadders(self, beginWord, endWord, wordList):
        adj_map = _build_adjacency_map(beginWord, wordList)
        return _find_ladders(adj_map, beginWord, endWord)
