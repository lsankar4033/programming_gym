from functools import reduce

with open('input.txt') as f:
    lines = f.readlines()

    cmds = [x.strip().split(' ') for x in lines]
    cmds = [(x[0], int(x[1])) for x in cmds]


def update(xya, cmd):
    x = xya[0]
    y = xya[1]
    aim = xya[2]
    if cmd[0] == 'up':
        return x, y, aim - cmd[1]
    elif cmd[0] == 'down':
        return x, y, aim + cmd[1]
    elif cmd[0] == 'forward':
        return x + cmd[1], y + (aim * cmd[1]), aim
    else:
        print(f'Invalid command {cmd}')


x, y, _ = reduce(lambda xya, cmd: update(xya, cmd), cmds, (0, 0, 0))

print(x * y)
