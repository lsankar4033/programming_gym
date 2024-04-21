with open('./input.txt', 'r') as file:
    lines = file.readlines()

matrix = [[c for c in line.strip()] for line in lines]

start_pos = (107, 110)  # where S is


class Dirs:
    U = (-1, 0)
    D = (1, 0)
    L = (0, -1)
    R = (0, 1)


cur_pos = start_pos  # where S is
cur_dir = Dirs.U


def update_dir(prev_dir, pos):
    pipe = matrix[pos[0]][pos[1]]
    if pipe == '|' or pipe == '-':
        return prev_dir

    match (pipe, prev_dir):
        case ('|', _):
            return prev_dir
        case ('-', _):
            return prev_dir

        case ('7', Dirs.R):
            return Dirs.D
        case ('7', Dirs.U):
            return Dirs.L

        case ('L', Dirs.D):
            return Dirs.R
        case ('L', Dirs.L):
            return Dirs.U

        case ('J', Dirs.D):
            return Dirs.L
        case ('J', Dirs.R):
            return Dirs.U

        case ('F', Dirs.U):
            return Dirs.R
        case ('F', Dirs.L):
            return Dirs.D

        case ('S', _):
            return Dirs.U

        case _:
            print(f"error! no match {pipe} {prev_dir}")
            exit(1)


# same as before, just keep track of all visited nodes
visited_nodes = {cur_pos}
while True:
    next_pos = (cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1])

    cur_pos = next_pos
    visited_nodes.add(cur_pos)

    cur_dir = update_dir(cur_dir, cur_pos)

    if cur_pos == start_pos:
        break

# now go through all indices and keep track of going in/out of the loop
contained = set()
for i in range(len(matrix)):
    within = False
    for j in range(len(matrix[i])):
        if (i, j) in visited_nodes:
            if matrix[i][j] in ['|', 'L', 'J']:
                within = not within
        elif within:
            contained.add((j, i))

print(len(contained))
