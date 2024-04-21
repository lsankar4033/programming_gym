
def calc_hash(cmd):
    ret = 0
    for c in cmd:
        ret += ord(c)
        ret = ret * 17
        ret = ret % 256

    return ret


with open('./input.txt', 'r') as file:
    lines = file.readlines()

commands = lines[0].split(',')

print(sum([calc_hash(cmd) for cmd in commands]))
