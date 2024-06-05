from functools import reduce

with open('input.txt') as f:
    lines = f.readlines()

    cmds = [x.strip().split(' ') for x in lines]
    cmds = [(x[0], int(x[1])) for x in cmds]


def update_xy(x, y, cmd):
    if cmd[0] == 'up':
        return x, y - cmd[1]
    elif cmd[0] == 'down':
        return x, y + cmd[1]
    elif cmd[0] == 'forward':
        return x + cmd[1], y
    else:
        print(f'Invalid command {cmd}')


x, y = reduce(lambda xy, cmd: update_xy(xy[0], xy[1], cmd), cmds, (0, 0))

print(x * y)
