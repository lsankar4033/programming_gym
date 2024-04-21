import re

with open('./input.txt', 'r') as file:
    lines = file.readlines()

NUM_RE = r'[0-9]+'

part_nums = []

for y, line in enumerate(lines):
    part_nums.extend([{
        'start_x': match.start(),
        'end_x': match.end(),
        'y': y,
        'num': int(match.group())
    } for match in re.finditer(NUM_RE, line.strip())])

def check_adjacent(gear_coord, part_num):
    x_in_range = gear_coord[0] >= part_num['start_x']-1 and gear_coord[0] <= part_num['end_x']
    y_in_range = gear_coord[1] >= part_num['y']-1 and gear_coord[1] <= part_num['y']+1
    return x_in_range and y_in_range

def get_adjacent_part_nums(gear_coord, part_nums):
    return [part_num['num'] for part_num in part_nums
        if check_adjacent(gear_coord, part_num)]

# for each gear, find adjacent 
# NOTE: can make faster by only checking adjacent y...
s = 0
for y, line in enumerate(lines):
    gear_coords = [(x, y) for x in range(len(line)) if line[x] == '*']

    for gear_coord in gear_coords:
        adjacent_part_nums = get_adjacent_part_nums(gear_coord, part_nums)
        if len(adjacent_part_nums) == 2:
            s += adjacent_part_nums[0] * adjacent_part_nums[1]
                   
print(s)