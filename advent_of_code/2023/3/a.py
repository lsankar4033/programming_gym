import re

with open('./input.txt', 'r') as file:
    lines = file.readlines()

PART_RE = r'[^0-9\.]'

def get_part_xs(line):
    return [match.start() for match in re.finditer(PART_RE, line.strip())]


def get_part_coords(lines):
    coords = []
    for y, line in enumerate(lines):
        xs = get_part_xs(line)

        coords.extend([(x, y) for x in xs])
    return coords

part_coords = get_part_coords(lines)

# for every int, check against parts

NUM_RE = r'[0-9]+'

def check_part_coord(start_x, end_x, y, part_coord):
    x_in_range = part_coord[0] >= start_x-1 and part_coord[0] <= end_x
    y_in_range = part_coord[1] >= y-1 and part_coord[1] <= y+1
    return x_in_range and y_in_range


def num_has_part(start_x, end_x, y, part_coords):
    return [part_coord for part_coord in part_coords if check_part_coord(start_x, end_x, y, part_coord)]

def find_part_nums(y, part_coords, line):
    nums = [{
        'start_x': match.start(),
        'end_x': match.end(),
        'num': int(match.group())
    } for match in re.finditer(NUM_RE, line.strip())]

    return [num['num'] for num in nums if num_has_part(num['start_x'], num['end_x'], y, part_coords)]

# print(part_coords)

s = 0
for y, line in enumerate(lines):
    nums = find_part_nums(y, part_coords, line)

    s += sum(nums)
    

print(s)