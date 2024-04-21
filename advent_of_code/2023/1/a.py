with open('./input.txt', 'r') as file:
    lines = file.readlines()

# map lines to filtered nums

def get_line_num(int_line):
    if len(int_line) == 0:
        print("found empty line!")
    elif len(int_line) == 1:
        return int(int_line[0] + int_line[0])
    else:
        return int(int_line[0] + int_line[-1])

int_lines = [[c for c in [*line] if c.isdigit()]
    for line in lines]

line_nums = [get_line_num(int_line) for int_line in int_lines]

print(sum(line_nums))