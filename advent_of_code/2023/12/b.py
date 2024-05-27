from functools import cache

with open('./input.txt', 'r') as file:
    lines = file.readlines()


@cache
def solve_line(line, nums):
    if not nums:
        return 0 if "#" in line else 1
    if not line:
        return 1 if not nums else 0

    result = 0

    if line[0] in ".?":
        result += solve_line(line[1:], nums)
    if line[0] in "#?":
        if (
            nums[0] <= len(line)
            and "." not in line[: nums[0]]
            and (nums[0] == len(line) or line[nums[0]] != "#")
        ):
            result += solve_line(line[nums[0] + 1:], nums[1:])

    return result


s = 0
for line in lines:
    l, nums = line.split()
    nums = eval(nums)

    s += solve_line("?".join([l] * 5), nums * 5)

print(s)
