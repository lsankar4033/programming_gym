with open('input.txt') as f:
    strs = [l.strip() for l in f.readlines()]


index_sets = []  # [(zero_indices, one_indices) for each index]
for i in range(len(strs[0])):
    index_sets.append({
        '0': set(),
        '1': set()
    })

for str_i, s in enumerate(strs):
    for c_i, c in enumerate(s):
        index_sets[c_i][c].add(str_i)


def get_counts(inds):
    # from previous problem
    counts = []
    for i in range(len(strs[0])):
        counts.append({
            '0': 0,
            '1': 0
        })

    _strs = [strs[i] for i in inds]
    for s in _strs:
        for i, c in enumerate(s):
            if c == '0':
                counts[i]['0'] += 1
            else:
                counts[i]['1'] += 1

    return counts


# o2 rating
cur_inds = set(range(len(strs)))
for i in range(len(strs[0])):
    counts = get_counts(cur_inds)

    c_i = counts[i]
    # handle ties! if both equal, take 1
    if c_i['0'] == c_i['1']:
        max_val = '1'
    else:
        max_val = max(c_i, key=c_i.get)

    filter_set = index_sets[i][max_val]

    cur_inds = cur_inds.intersection(filter_set)

    if (len(cur_inds) == 1):
        o2_ind = list(cur_inds)[0]
        break


# co2 rating
cur_inds = set(range(len(strs)))
for i in range(len(strs[0])):
    counts = get_counts(cur_inds)

    c_i = counts[i]
    # handle ties! if both equal, take 1
    if c_i['0'] == c_i['1']:
        min_val = '0'
    else:
        min_val = min(c_i, key=c_i.get)

    filter_set = index_sets[i][min_val]

    cur_inds = cur_inds.intersection(filter_set)

    if (len(cur_inds) == 1):
        co2_ind = list(cur_inds)[0]
        break


o2_rating = int(strs[o2_ind], 2)
co2_rating = int(strs[co2_ind], 2)
print(o2_rating * co2_rating)
