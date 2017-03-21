# Challenge here: https://www.hackerrank.com/challenges/gridland-metro
import sys

from collections import defaultdict

# Return a new list of segments
def add_segment(existing_segments, new_segment):
    # get segments that intersect with both front and back and properly take the endpoints

    return []

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
