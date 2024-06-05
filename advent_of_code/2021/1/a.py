with open('input.txt') as f:
    lines = f.readlines()
    nums = [int(x.strip()) for x in lines]

diffs = [nums[x] - nums[x-1] for x in range(1, len(nums))]

print(len([x for x in diffs if x > 0]))
