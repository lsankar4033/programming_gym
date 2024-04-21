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


steps = 0
while True:
    next_pos = (cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1])

    cur_pos = next_pos
    cur_dir = update_dir(cur_dir, cur_pos)
    steps += 1

    if cur_pos == start_pos:
        break

print(steps / 2)
