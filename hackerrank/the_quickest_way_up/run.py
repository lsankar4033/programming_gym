# Challenge here: https://www.hackerrank.com/challenges/the-quickest-way-up
# Solution involves creating a graph and doing BFS. Graph must be altered based on snakes/ladders so that edge
# pointing to the start of a snake/ladder actually points to its end and all start points are just removed.

import sys

BOARD_SIZE = 10 # 10 x 10

# snakes, ladders are both lists of tuples
def build_graph(snakes, ladders):
    adjacency_map = {}
    reverse_adjacency_map = {} # used to quickly do snake/ladder xforms

    # init empty board
    for i in range(1, BOARD_SIZE * BOARD_SIZE + 1):
        adjacency_map[i] = set([i + j for j in range(1, 7) if i + j <= 100])
        reverse_adjacency_map[i] = set([i - j for j in range(1, 7) if i - j >= 1])

    # NOTE this assumes (as the problem statement does) that the end of any snake/ladder isn't the start of
    # another
    snake_ladders = snakes + ladders
    for (s, e) in snake_ladders:
        # connect all nodes pointing to start to end
        for r in reverse_adjacency_map[s]:
            adjacency_map[r].add(e)
            adjacency_map[r].remove(s)

    for (s, _) in snake_ladders:
        del adjacency_map[s]

    return adjacency_map

# Return the number of steps in the min path from start -> end. If no path exists, return -1
def get_shortest_path_length(adjacency_map, start, end):
    visited = set()
    frontier = {start}
    path_length = 0

    while len(frontier) > 0:
        if end in frontier:
            return path_length
        else:
            neighbors = {n for f in frontier for n in adjacency_map[f]}
            visited |= frontier
            frontier = neighbors - visited
            path_length += 1

    # end wasn't reachable from start
    return -1

# TODO - these could be moved into utilities if I keep doing hackerrank problems
def get_int_from_stdin():
    return int(sys.stdin.readline().strip())

def get_tuple_from_stdin():
    l = sys.stdin.readline().strip()
    return [int(i) for i in l.split(" ")]

if __name__ == "__main__":
    num_problems = get_int_from_stdin()

    for i in range(num_problems):
        # get snakes
        num_snakes = get_int_from_stdin()
        snakes = []
        for j in range(num_snakes):
            snakes.append(get_tuple_from_stdin())

        # get ladders
        num_ladders = get_int_from_stdin()
        ladders = []
        for j in range(num_ladders):
            ladders.append(get_tuple_from_stdin())

        adjacency_map = build_graph(snakes, ladders)
        path_length = get_shortest_path_length(adjacency_map, 1, 100)

        print(path_length)
