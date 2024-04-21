from itertools import cycle

# read input
with open('./input.txt', 'r') as file:
    lines = file.readlines()
move_iter = cycle(
    [int(c) for c in lines[0].strip().replace('L', '0').replace('R', '1')]
)
node_map = {}
for line in lines[2:]:
    src, dst_str = line.split(' = ')
    node_map[src] = dst_str[1:-2].split(', ')

# starting with AAA, follow move iter until we hit ZZZ
# count steps
steps = 0
cur_node = 'AAA'

for move in move_iter:
    cur_node = node_map[cur_node][move]
    steps += 1

    if cur_node == 'ZZZ':
        break

print(steps)
