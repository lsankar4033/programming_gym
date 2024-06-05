with open('input.txt') as f:
    lines = f.readlines()
    nums = [int(x.strip()) for x in lines]

trips = [(nums[x-2], nums[x - 1], nums[x]) for x in range(2, len(nums))]
sums = [sum(x) for x in trips]

diffs = [sums[x] - sums[x-1] for x in range(1, len(sums))]

print(len([x for x in diffs if x > 0]))
