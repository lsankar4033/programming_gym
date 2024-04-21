# NOTE: puzzle input
maxes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open('./input.txt', 'r') as file:
    lines = file.readlines()

    

def process_line(line):
    # split into game_id and games
    s0 = line.split(':')
    game_id = s0[0].strip().split(' ')[1]
    
    # split games
    s1 = s0[1].strip().split(';')

    # nested for here sucks...
    for game_strs in s1:
        cube_count_strs = [c.strip() for c in game_strs.strip().split(',')]
        for cube_count_str in cube_count_strs:
            (count, color) = cube_count_str.split(' ')
            if int(count) > maxes[color]:
                return (game_id, False)
    
    return (int(game_id), True) 

results = [process_line(line) for line in lines]

valid_games = [r[0] for r in results if r[1] == True]
print(sum(valid_games))
