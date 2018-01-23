from collections import defaultdict, deque

def build_adj_map(edges):
    adj_map = defaultdict(set)

    for n0, n1 in edges:
        adj_map[n0].add(n1)
        adj_map[n1].add(n0)

    return adj_map


def get_distances(start_node, num_nodes, edges):
    adj_map = build_adj_map(edges)

    distances = []
    for n in range(1, num_nodes + 1):
        if n == start_node:
            continue

        distances.append(bfs(start_node, n, adj_map))

    return distances

def bfs(start, end, adj_map):
    visited = set()
    queue = deque([(start, 0)])

    while len(queue) > 0:
        n, dist = queue.popleft()

        if n == end:
            return dist

        visited.add(n)
        candidates = [(node, 6 + dist) for node in adj_map[n] - visited]

        queue.extend(candidates)

    return -1

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        edges = []
        for edges_i in range(m):
            edges_t = [int(edges_temp) for edges_temp in input().strip().split(' ')]
            edges.append(edges_t)
        s = int(input().strip())

        # change this
        result = get_distances(s, n, edges)
        print (" ".join(map(str, result)))
