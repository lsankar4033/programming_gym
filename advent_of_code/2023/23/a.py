import sys
with open('input.txt') as f:
    lines = f.readlines()

grid = [[c for c in line.strip()] for line in lines]

start_coord = (0, grid[0].index('.'))
end_coord = (len(grid) - 1, grid[-1].index('.'))


def get_prev(coord):
    # possible prev paths. handle '>' etc. cases
    match grid[coord[0]][coord[1]]:
        case '>':
            candidates = {(coord[0], coord[1] - 1)}
        case '<':
            candidates = {(coord[0], coord[1] + 1)}
        case '^':
            candidates = {(coord[0] + 1, coord[1])}
        case 'v':
            candidates = {(coord[0] - 1, coord[1])}

        case '.':
            candidates = {
                (coord[0], coord[1] - 1),
                (coord[0], coord[1] + 1),
                (coord[0] + 1, coord[1]),
                (coord[0] - 1, coord[1]),
            }

        case '#':
            print("error! attempting to get prev for '#'")
            exit(1)

    # filter out '#', out of bounds, from candidatesreturn
    return set([c for c in candidates
                if c[0] >= 0 and c[1] >= 0 and c[0] < len(grid) and c[1] < len(grid[0])
                and grid[c[0]][c[1]] != '#'])


def max_path(coord, avoid_coords=set()):
    # longest path to a given coord. 'avoid_coords' represents coords path hits in the future
    if coord == start_coord:
        return 0
    else:
        prev_coords = get_prev(coord)
        possible_prev_coords = prev_coords - avoid_coords

        if len(possible_prev_coords) == 0:
            return 0

        max_prev = max([max_path(prev_coord, avoid_coords | {
                       coord}) for prev_coord in possible_prev_coords])

        return 1 + max_prev


print(max_path(end_coord))
