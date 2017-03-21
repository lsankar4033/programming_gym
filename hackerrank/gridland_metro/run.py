# Challenge here: https://www.hackerrank.com/challenges/gridland-metro
import sys

from collections import defaultdict
from itertools import filterfalse

# Return a new list of segments
def add_segment(existing_segments, new_segment):

    def segment_intersects(segment):
        (sc1, sc2) = segment
        return (sc2 >= nc1 and sc2 <= nc2) or (sc1 >= nc1 and sc1 <= nc2)

    (nc1, nc2) = new_segment

    intersecting = list(filter(segment_intersects, existing_segments))
    non_intersecting = list(filterfalse(segment_intersects, existing_segments))

    if len(intersecting) == 0:
        new_c1 = nc1
        new_c2 = nc2
    else:
        new_c1 = min([c1 for (c1, c2) in intersecting] + [nc1])
        new_c2 = max([c2 for (c1, c2) in intersecting] + [nc2])

    non_intersecting.append((new_c1, new_c2))
    return non_intersecting

# each train track is a tuple of (r, c1, c2)
def get_num_used_squares(train_tracks):

    # create map from row -> [segment] where each segment is a [start,end] tuple
    row_to_segments = defaultdict(list)
    for (r, c1, c2) in train_tracks:
        row_to_segments[r] = add_segment(row_to_segments[r], (c1, c2))

    # count used cells by going through map

    pass

# NOTE - this method is just copied around in all hackerrank modules
def get_tuple_from_stdin():
    l = sys.stdin.readline().strip()
    return [int(i) for i in l.split(" ")]

if __name__ == "__main__":
    pass
