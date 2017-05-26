# Problem here: https://leetcode.com/problems/find-peak-element/#/description
from math import ceil, floor
from statistics import mean

class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1
        else:

            i = floor(len(nums) / 2)
            start = 0
            end = len(nums)
            while True:
                if i == 0 or i == len(nums) - 1:
                    return i

                p = nums[i-1]
                c = nums[i]
                n = nums[i+1]

                if c > n and c > p:
                    return i
                elif c > p and n > c:
                    start = i
                    i = ceil( mean([i, end]) )
                # NOTE: valley means we can pick arbitrarily
                else:
                    end = i
                    i = floor( mean([start, i]) )
