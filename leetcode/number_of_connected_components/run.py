# Problem here: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/#/description
# Time taken: 11 minutes

def build_adj_map(n, edges):
    adj_map = {}
    for i in range(n):
        adj_map[i] = set()

    for (n1, n2) in edges:
        adj_map[n1].add(n2)
        adj_map[n2].add(n1)

    return adj_map

def get_connected_component(adj_map, start_node):
    visited = set()
    frontier = [start_node]
    while len(frontier) > 0:
        cur_node = frontier.pop()
        if cur_node in visited:
            continue
        visited.add(cur_node)

        neighbors = adj_map[cur_node]
        frontier += list(neighbors - visited)

    return visited

def count_connected_components(n, edges):
    adj_map = build_adj_map(n, edges)

    remaining_nodes = set(list(range(n)))
    num_connected_components = 0
    while len(remaining_nodes) > 0:
        start_node = remaining_nodes.pop()
        connected_component = get_connected_component(adj_map, start_node)
        remaining_nodes -= connected_component
        num_connected_components += 1

    return num_connected_components
