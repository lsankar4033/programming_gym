import re
import math

with open('./input.txt', 'r') as file:
    lines = file.readlines()

INT_REPLACEMENTS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

INT_KEYS = list(INT_REPLACEMENTS.keys())

def cluster_string(s):
    pattern = r'\d+|\D+'
    clusters = re.findall(pattern, s)
    return clusters


def get_first_last_digit(cluster):
    if cluster.isdigit():
        return (cluster[0], cluster[-1])

    else:
        int_locs = [(int_key, [m.start() for m in re.finditer(int_key, cluster)])
            for int_key in INT_KEYS]
        nonempty_int_locs = [(int_key, locs) for int_key, locs in int_locs if len(locs) > 0]

        min_loc = math.inf
        min_int_key = None
        max_loc = -1
        max_int_key = None
        for int_key, locs in nonempty_int_locs:
            if min(locs) < min_loc:
                min_int_key = int_key
                min_loc = min(locs)
            if max(locs) > max_loc:
                max_loc = max(locs)
                max_int_key = int_key
        if min_int_key is not None and max_int_key is not None:
            return (INT_REPLACEMENTS[min_int_key], INT_REPLACEMENTS[max_int_key])
        
        else:
            return (None, None)


def get_line_num(line):
    clusters = cluster_string(line)

    cluster_first_lasts = [get_first_last_digit(cluster) for cluster in clusters]
    filter_nones = [first_last for first_last in cluster_first_lasts if first_last[0] is not None and first_last[1] is not None]

    if (len(filter_nones) == 0):
        print("No valid clusters found in line!", line)
        return 0

    first = filter_nones[0][0]
    last = filter_nones[-1][-1]

    return int(first + last)
    
line_nums = [get_line_num(line) for line in lines]

print(sum(line_nums))
