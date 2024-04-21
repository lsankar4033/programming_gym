from itertools import cycle
import math

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

# start at all nodes ending in A
steps = 0
cur_nodes = [node for node in node_map.keys() if node[-1] == 'A']
# for each node, mark the cycle length at the first cycle
cycle_lengths = [math.inf for _ in cur_nodes]

# # NOTE: might need to find the cycle for each and do a lcm
for move in move_iter:
    next_nodes = [node_map[cur_node][move] for cur_node in cur_nodes]
    cur_nodes = next_nodes
    steps += 1

    if any([node[-1] == 'Z' for node in cur_nodes]):
        indices = [i for i, node in enumerate(cur_nodes) if node[-1] == 'Z']
        for i in indices:
            cycle_lengths[i] = steps

        if all([cycle_length != math.inf for cycle_length in cycle_lengths]):
            break

print(f"cycle lengths: {cycle_lengths}")


def __gcd(a, b):
    if (a == 0):
        return b
    return __gcd(b % a, a)


def lcm(arr, idx):

    # lcm(a,b) = (a*b/gcd(a,b))
    if (idx == len(arr)-1):
        return arr[idx]
    a = arr[idx]
    b = lcm(arr, idx+1)
    return int(a*b/__gcd(a, b))  # __gcd(a,b) is inbuilt library function


print(lcm(cycle_lengths, 0))
