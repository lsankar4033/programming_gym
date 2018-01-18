from collections import deque

import sys

# NOTE: 2-way DFS would be faster, but let's start with 1-way

def get_neighbors(x, y, i, j, n):
    # could be cleaner...
    candidates = [(x + i, y + j), (x + i, y - j), (x - i, y + j), (x - i, y - j),
                  (x + j, y + i), (x + j, y - i), (x - j, y + i), (x - j, y - i)]

    return set([(x, y) for (x, y) in candidates if x > -1 and x < n and y > -1 and y < n])

def compute_min_distance(i, j, n):
    queue = deque([(0, 0, 0)]) # (i,j,dist)
    visited = set()

    while len(queue) > 0:
        x, y, dist = queue.popleft()

        if (x,y) not in visited:
            visited.add((x,y))
            neighbors = get_neighbors(x, y, i, j, n) - visited

            if (n - 1, n - 1) in neighbors:
                return dist + 1

            queue.extend([(xn, yn, dist + 1) for (xn, yn) in neighbors])

    return -1

n = int(input().strip())

memoized = {}
for i in range(1, n):
    for j in range(i, n):
        dist = compute_min_distance(i, j, n)

        memoized[(i, j)] = dist
        memoized[(j, i)] = dist

for i in range(1, n):
    dists = [memoized[(i, j)] for j in range(1, n)]

    print(" ".join([str(d) for d in dists]))
