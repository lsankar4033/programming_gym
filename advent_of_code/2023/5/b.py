import itertools 
import functools

with open('./input.txt', 'r') as file:
    lines = file.readlines()

# group by double newline
group_lines = [list(g) for k, g in itertools.groupby(lines, lambda x: x == '\n') if not k]

def flatten(xss):
    return [x for xs in xss for x in xs]

def get_seed_ranges(seed_lines):
    seed_line = seed_lines[0]
    seed_str = seed_line.split(':')[1].strip()
    seed_str_nums = [int(s) for s in seed_str.split(' ')]

    start_range_tuples = list(zip(*(iter(seed_str_nums),) * 2))

    # start, end tuples
    return [(s[0], s[0] + s[1]) for s in start_range_tuples]

seed_ranges = get_seed_ranges(group_lines[0])

def build_map_fn(map_lines):
    sorted_segments = [
        [int(s.strip()) for s in segment.split(' ')]
        for segment in map_lines[1:]
    ]

    # below closure fns act on this data
    # (dst, src, len)
    sorted_segments.sort(key=lambda x: x[1])

    def get_seg_ind(x):
        for i, seg in enumerate(sorted_segments):
            if x >= seg[1] and x < seg[1] + seg[2]:
                return i

        return -1

    def split_range(range_pair):
        start_seg_ind = get_seg_ind(range_pair[0])
        end_seg_ind = get_seg_ind(range_pair[1])


        # if both outside range, return original range pair
        if start_seg_ind == -1 and end_seg_ind == -1:
            return [range_pair]

        # single segment
        elif start_seg_ind == end_seg_ind:
            seg = sorted_segments[start_seg_ind]
            return [(
                seg[0] + (range_pair[0] - seg[1]), 
                seg[0] + (range_pair[1] - seg[1])
            )]

        else:
            range_pairs = []
            
            # add start range
            if start_seg_ind == -1:
                # start -> src of first segment
                range_pairs.append((
                    range_pair[0], sorted_segments[0][1]
                ))
            else:
                start_seg = sorted_segments[start_seg_ind]
                range_pairs.append((
                    start_seg[0] + (range_pair[0] - start_seg[1]), # start within dst
                    start_seg[0] + start_seg[2] # end of dst 
                ))

            # add middle ranges. these are just the dsts of the internal segs
            for i in range(start_seg_ind + 1, end_seg_ind):
                seg = sorted_segments[i]
                range_pairs.append((
                    seg[0], seg[0] + seg[2]
                ))

            # add end range
            if end_seg_ind == -1:
                # end seg src -> end
                range_pairs.append((
                    sorted_segments[-1][1], range_pair[1]
                ))
            else:
                end_seg = sorted_segments[end_seg_ind]
                range_pairs.append((
                    end_seg[0], # end dst
                    end_seg[0] + (range_pair[1] - end_seg[1]) # end within dst
                ))
            
            return range_pairs

    def split_range_pairs(range_pairs):
        # for each range_pair, split ranges, mapcat
        return flatten(map(split_range, range_pairs))

    return split_range_pairs

map_fns = [build_map_fn(group) for group in group_lines[1:]]

all_ranges = flatten([
    functools.reduce(
        lambda x, f: f(x),
        map_fns, 
        [seed_range]
        )
    for seed_range in seed_ranges
])

print(min(all_ranges, key=lambda r: r[0]))