# Challenge here: https://www.hackerrank.com/challenges/the-quickest-way-up
# Solution involves creating a graph and doing BFS. Graph must be altered based on snakes/ladders so that edge
# pointing to the start of a snake/ladder actually points to its end and all start points are just removed.

BOARD_SIZE = 4 # 10 x 10

# snakes, ladders are both lists of tuples
def build_graph(snakes, ladders):
    # graph nodes are 1-indexed

    # build adjacency map and reverse adjacency amp
    adjacency_map = {}
    reverse_adjacency_map = {} # used to quickly do snake/ladder xforms

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

        del adjacency_map[s]

    return adjacency_map

# Return the number of steps in the min path from start -> end. If no path exists, return -1
def run_bfs(adjacency_map, start, end):
    pass
