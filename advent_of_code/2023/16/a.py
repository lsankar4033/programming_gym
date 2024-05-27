from collections import deque, defaultdict

with open("input.txt") as file:
    lines = file.readlines()
    symbols = [[*line.strip()] for line in lines]


def get_next(p, d):
    symbol = symbols[p[0]][p[1]]

    if symbol == '.':
        return [((p[0] + d[0], p[1] + d[1]), d)]

    elif symbol == '/':
        # (0, 1) -> (-1, 0)
        # (0, -1) -> (1, 0)
        # (1, 0) -> (0, -1)
        # (-1, 0) -> (0, 1)
        new_d = (-1 * d[1], -1 * d[0])
        return [((p[0] + new_d[0], p[1] + new_d[1]), new_d)]

    elif symbol == '\\':
        new_d = (d[1], d[0])
        return [((p[0] + new_d[0], p[1] + new_d[1]), new_d)]

    elif symbol == '|':
        if d == (0, 1) or d == (0, -1):
            return [((p[0] + 1, p[1]), (1, 0)),
                    ((p[0] - 1, p[1]), (-1, 0))]

        else:
            return [((p[0] + d[0], p[1] + d[1]), d)]
    elif symbol == '-':
        if d == (1, 0) or d == (-1, 0):
            return [((p[0], p[1] + 1), (0, 1)),
                    ((p[0], p[1] - 1), (0, -1))]
        else:
            return [((p[0] + d[0], p[1] + d[1]), d)]

    else:
        print("Unknown symbol", symbol)
        exit(1)


def in_grid(pos):
    return pos[0] >= 0 and pos[0] < len(
        symbols) and pos[1] >= 0 and pos[1] < len(symbols[0])


visited = defaultdict(set)  # pos -> set(dir_tuples)
to_visit = deque([((0, 0), (0, 1))])  # start at 0, 0, facing right

while len(to_visit) != 0:
    cur_pos, cur_dir = to_visit.popleft()

    if cur_dir in visited[cur_pos] or not in_grid(cur_pos):
        continue

    visited[cur_pos].add(cur_dir)

    n = get_next(cur_pos, cur_dir)

    to_visit.extendleft(get_next(cur_pos, cur_dir))


# return all in visited with nonzero val set
visited_p = [k for k in visited.keys() if len(visited[k]) > 0]
print(len(visited_p))
