import itertools 
import functools

with open('./input.txt', 'r') as file:
    lines = file.readlines()

# group by double newline
group_lines = [list(g) for k, g in itertools.groupby(lines, lambda x: x == '\n') if not k]

def process_seeds(seed_lines):
    seed_line = seed_lines[0]
    seed_str = seed_line.split(':')[1].strip()
    return [int(s.strip()) for s in seed_str.split(' ')]

seeds = process_seeds(group_lines[0])

def process_map(map_lines):
    # (dst, src, len), sort by src
    sorted_segments = [
        [int(s.strip()) for s in segment.split(' ')]
        for segment in map_lines[1:]
    ]

    sorted_segments.sort(key=lambda x: x[1])

    def map_fn(x):
        for seg in sorted_segments:
            # if x in range of segment
            if x >= seg[1] and x < seg[1] + seg[2]:
                return seg[0] + x - seg[1]

        # otherwise just return x
        return x

    return map_fn

map_fns = [process_map(group) for group in group_lines[1:]]
locations = [
    functools.reduce(
        lambda x, f: f(x),
        map_fns, 
        seed
        )
    for seed in seeds
]

print(min(locations))
