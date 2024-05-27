from collections import defaultdict

with open('./input.txt', 'r') as file:
    lines = file.readlines()

start_coord = None
coord_map = defaultdict(list)

for (y, line) in enumerate(lines):
    for (x, char) in enumerate(line.strip()):
        if char == 'S':
            start_coord = (x, y)

        if char == '#':
            continue

        for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x = x + dx
            new_y = y + dy

            if new_x < 0 or new_y < 0 or new_x >= len(line) or new_y >= len(lines):
                continue

            if lines[new_y][new_x] != '#':
                coord_map[(x, y)].append((new_x, new_y))

coords = set([start_coord])

# 64 step bfs
for i in range(64):
    print(i, len(coords))
    new_coords = set()

    for coord in coords:
        for new_coord in coord_map[coord]:
            new_coords.add(new_coord)

    coords = new_coords

print(len(new_coords))
