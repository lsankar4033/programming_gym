import re 

with open('./input.txt', 'r') as file:
    lines = file.readlines()


NUM_RE = r'[0-9]+'

def get_num_wins(card_line):
    s0 = card_line.split(":")
    s1 = s0[1].split("|")

    winning_nums = set(re.findall(NUM_RE, s1[0]))
    my_nums = re.findall(NUM_RE, s1[1]) 

    return len([n for n in my_nums if n in winning_nums])

def get_total_copies(card_num, card_to_copies):
    # recursively add all cards to total
    if card_num not in card_to_copies:
        raise ValueError(f"error! couldn't find card in map {card_num}")
        return 0

    copies = card_to_copies[card_num]
    if len(copies) == 0:
        return 1
    else:
        return 1 + sum(
            get_total_copies(c, card_to_copies) for c in copies
        )

card_to_copies = {} # card -> [card]  
total_cards = 0

for i, line in reversed(list(enumerate(lines))):
    card_num = i + 1 # not strictly necessary, but makes debugging easier 

    num_wins = get_num_wins(line)
    if num_wins > 0:
        card_to_copies[card_num] = list(
            range(card_num + 1, card_num + num_wins + 1)
        )

        total_cards += get_total_copies(card_num, card_to_copies)

    else:
        card_to_copies[card_num] = []

print(total_cards)
