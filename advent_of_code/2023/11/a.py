from itertools import combinations

with open('./test_input.txt', 'r') as file:
    lines = file.readlines()

coords = [[c for c in l.strip()] for l in lines]

# first, expansion
galaxy_rows = set()
galaxy_cols = set()
for i in range(len(coords)):
    for j in range(len(coords[i])):
        if coords[i][j] == '#':
            galaxy_rows.add(i)
            galaxy_cols.add(j)

missing_rows = [i for i in range(len(coords)) if i not in galaxy_rows]
missing_cols = [j for j in range(len(coords[0])) if j not in galaxy_cols]

print(missing_cols)

# expand cols
for row in coords:
    for col in missing_cols:
        row.insert(col+1, '.')

# expand rows
for row in missing_rows:
    coords.insert(row+1, ['.']*len(coords[0]))

# TODO: expansion isn't working properly

galaxy_coords = []
for i in range(len(coords)):
    for j in range(len(coords[i])):
        if coords[i][j] == '#':
            galaxy_coords.append((i, j))

sum = 0
for g1, g2 in combinations(galaxy_coords, 2):
    dist = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    # print(f'{g1} -> {g2}: {dist}')

    sum += dist

print(sum)
