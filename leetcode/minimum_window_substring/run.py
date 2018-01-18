from collections import defaultdict

def filtered_index_tuples(s, t):
    return [(i, c) for (i, c) in enumerate(s) if c in set(t)]

def count_dict_covers_target(count_dict, target_dict):
    return all(count_dict[c] >= n for (c, n) in target_dict.items())

def str_to_count_dict(s):
    ret = defaultdict(lambda: 0)
    for c in s:
        ret[c] += 1
    return ret

def min_window(s, t):
    """s is whole string, t is substring.
    """
    if len(s) == 0 or len(t) == 0:
        return ''
    elif len(t) == 1:
        if t[0] in s:
            return t
        else:
            return ''

    index_tuples = filtered_index_tuples(s, t)
    if len(index_tuples) < len(t):
        return ''

    count_dict = defaultdict(lambda: 0)
    target_dict = str_to_count_dict(t)
    start = 0
    end = 0
    count_dict[index_tuples[start][1]] += 1
    best = (-1, len(s)) # nonsensical
    while end < len(index_tuples): #or count_dict_covers_target(count_dict, t):
        covers_target = count_dict_covers_target(count_dict, target_dict)

        if covers_target:
            if index_tuples[end][0] - index_tuples[start][0] < best[1] - best[0]:
                best = (index_tuples[start][0], index_tuples[end][0])

            count_dict[index_tuples[start][1]] -= 1
            start += 1
        else:
            end += 1
            if end < len(index_tuples):
                count_dict[index_tuples[end][1]] += 1

    if best[0] == -1:
        return ''
    else:
        return s[best[0]:best[1] + 1]
