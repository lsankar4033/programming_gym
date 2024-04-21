import re
from collections import namedtuple


def calc_hash(label):
    ret = 0
    for c in label:
        ret += ord(c)
        ret = ret * 17
        ret = ret % 256

    return ret


with open('./input.txt', 'r') as file:
    lines = file.readlines()

commands = lines[0].split(',')


def parse_label(cmd):
    alpha_pattern = re.compile(r'[a-zA-Z]+')
    m = alpha_pattern.search(cmd)

    return m.group()


Lens = namedtuple('Lens', ['label', 'focal_length'])

boxes = [[]] * 256
for command in commands:
    label = parse_label(command)
    box = calc_hash(label)

    if '=' in command:
        old_box = boxes[box]
        if not any(l.label == label for l in old_box):
            boxes[box].append(
                Lens(label=label, focal_length=int(command.split('=')[1])))

        else:
            old_ind = [i for i, l in enumerate(old_box) if l.label == label][0]
            boxes[box][old_ind] = Lens(
                label=label, focal_length=int(command.split('=')[1]))

    elif '-' in command:
        old_box = boxes[box]
        boxes[box] = [l for l in old_box if l.label != label]
    else:
        print('Invalid command', command)
        exit(1)

power = 0
for i, box in enumerate(boxes):
    box_num = i + 1
    for j, lens in enumerate(box):
        lens_num = j + 1
        power += box_num * lens.focal_length * lens_num

print(power)
