def get_distance(hold_time, race_time):
    return (race_time - hold_time) * hold_time

def get_win_count(race_time, target_distance):
    win_count = 0

    # optimize by stopping check once outside window
    for hold_time in range(race_time):
        dist = get_distance(hold_time, race_time)

        if dist > target_distance:
            win_count += 1
    
    return win_count

# print(get_win_count(71530, 940200))

# Time:        53     71     78     80
# Distance:   275   1181   1215   1524

print(get_win_count(53717880, 275118112151524))
