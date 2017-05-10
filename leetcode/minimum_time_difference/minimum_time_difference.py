from itertools import combinations

FULL_DAY_MINS = 24 * 60

def _time_str_to_mins(t_str):
    (h, m) = [int(i) for i in t_str.split(":")]
    return h * 60 + m

class Solution(object):
    def findMinDifference(self, timePoints):
        mins = [_time_str_to_mins(tp) for tp in timePoints]
        mins.sort()

        min_diff = (mins[0] - mins[-1]) % FULL_DAY_MINS
        for i in range(len(mins) - 1):
            min_diff = min(min_diff, mins[i+1] - mins[i])

        return min_diff
