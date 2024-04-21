import re 

with open('./input.txt', 'r') as file:
    lines = file.readlines()


NUM_RE = r'[0-9]+'
    
def get_points(card):
    s0 = card.split(":")
    
    s1 = s0[1].split("|")

    winning_nums = set(re.findall(NUM_RE, s1[0]))
    my_nums = re.findall(NUM_RE, s1[1]) 

    num_wins = len([n for n in my_nums if n in winning_nums])

    score = 2**(num_wins-1) if num_wins > 0 else 0

    return score 
   

s = 0
for line in lines:
    s += get_points(line)
    
print(s)
    
