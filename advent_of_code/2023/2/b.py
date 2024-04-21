import math 

with open('./input.txt', 'r') as file:
    lines = file.readlines()

def min_game_power(line):
    # split into game_id and games
    s0 = line.split(':')
    
    # split games
    s1 = s0[1].strip().split(';')


    mins = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    

    # nested for here sucks...
    for game_strs in s1:
        cube_count_strs = [c.strip() for c in game_strs.strip().split(',')]
        for cube_count_str in cube_count_strs:
            (count, color) = cube_count_str.split(' ')
            if int(count) > mins[color]:
                mins[color] = int(count)

    return mins['red'] * mins['green'] * mins['blue']

powers = [min_game_power(line) for line in lines]

print(sum(powers))
