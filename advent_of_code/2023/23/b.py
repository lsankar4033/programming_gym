from collections import defaultdict, deque

with open('input.txt') as f:
    lines = f.readlines()

grid = [[c for c in line.strip()] for line in lines]

# NOTE: may want to do edge contraction idea here.
# do bfs from start to end, each time there's a choice, collapse coords into a node in the graph and create edges to choice
# if visited, don't revisit


def get_adjacent(i, j):
    candidates = [
        (i, j - 1),
        (i, j + 1),
        (i + 1, j),
        (i - 1, j),
    ]
    return [c for c in candidates
            if 0 <= c[0] < len(grid) and 0 <= c[1] < len(grid[0])
            and grid[c[0]][c[1]] != '#']


def find_vertices():
    # find each point in grid that has multiple neighbors
    vertices = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                continue

            adjacent = get_adjacent(i, j)
            if len(adjacent) > 2:
                vertices.add((i, j))

    start_coord = (0, grid[0].index('.'))
    end_coord = (len(grid) - 1, grid[-1].index('.'))

    return vertices | {start_coord, end_coord}


def generate_edges(vertices):
    edges = defaultdict(set)
    # bfs from each vertex to others to determine weighted edges b/w them
    for vertex in vertices:
        # do bfs from vertex to all other vertices
        visited = set()
        queue = deque([(vertex, 0)])

        while queue:
            (i, j), dist = queue.popleft()

            if (i, j) in visited:
                continue

            visited.add((i, j))

            for adj in get_adjacent(i, j):
                if adj in vertices and adj != vertex:
                    edges[vertex].add((adj, dist + 1))
                else:
                    queue.append((adj, dist + 1))

    return edges


def dfs(grid, edges, start, end, visited=set()):
    if start == end:
        return [0]

    visited.add(start)
    path_lengths = []

    for adj, dist in edges[start]:
        if adj not in visited:
            for path_len in dfs(grid, edges, adj, end, visited):
                # adjust each length by adding the current dist
                path_lengths.append(path_len + dist)

    visited.remove(start)  # to allow other paths to visit this vertex

    return path_lengths


vertices = find_vertices()

edges = generate_edges(vertices)

start_coord = (0, grid[0].index('.'))
end_coord = (len(grid) - 1, grid[-1].index('.'))

paths = dfs(grid, edges, start_coord, end_coord)

print(paths)
print(max(paths))
