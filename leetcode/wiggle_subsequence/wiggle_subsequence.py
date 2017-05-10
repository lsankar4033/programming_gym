from itertools import groupby

def _sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

class Solution(object):
    def wiggleMaxLength(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        differences = (nums[i+1] - nums[i] for i in range(len(nums) - 1))
        signs = (_sign(d) for d in differences if _sign(d) != 0)
        return len(list(groupby(signs))) + 1
