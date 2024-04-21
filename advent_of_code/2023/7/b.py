from functools import cmp_to_key

from collections import namedtuple, Counter
from enum import Enum

# NOTE: sorted by rank
HandType = Enum('HandType', 
                    [
                        'hc', # high card
                        '1p', # one pair
                        '2p', # two pair
                        '3ok', # three of a kind
                        'fh', # full house
                        '4ok', # four of a kind
                        '5ok' # five of a kind
                    ])
Hand = namedtuple('Hand', ['type', 'digits', 'bid'])

def char_to_digit(c):
    if c.isdigit():
        return int(c)
    elif c == 'T':
        return 10
    elif c == 'J':
        return 1 # NOTE: joker
    elif c == 'Q':
        return 12
    elif c == 'K':
        return 13
    elif c == 'A':
        return 14

def hand_str_to_digits(hand_str):
    return [char_to_digit(c) for c in hand_str]

def is_4ok(digits):
    srt = sorted(digits)
    return srt[0] == srt[3] or srt[1] == srt[4]

def is_fh(digits):
    srt = sorted(digits)
    return srt[0] == srt[2] and srt[3] == srt[4] or srt[0] == srt[1] and srt[2] == srt[4] 

def is_3ok(digits):
    srt = sorted(digits)
    return srt[0] == srt[2] or srt[1] == srt[3] or srt[2] == srt[4]

def digits_to_type(digits):
    if len(set(digits)) == 1:
        return HandType['5ok']

    elif is_4ok(digits):
        return HandType['4ok']

    elif is_fh(digits):
        return HandType['fh']

    elif is_3ok(digits):
        return HandType['3ok']

    elif len(set(digits)) == 3:
        return HandType['2p']

    elif len(set(digits)) == 4:
        return HandType['1p']

    else:
        return HandType['hc']

def jokerized_digits(digits):
    if 1 not in digits:
        return digits

    elif len(set(digits)) == 1:
        # NOTE: all jokers
        return digits

    else:
        card_count = Counter(digits)
        del card_count[1] # remove jokers
        most_common_card = card_count.most_common(1)[0][0]

        return [most_common_card if d == 1 else d for d in digits]

def line_to_hand(line):
    (hand_str, bid_str) = line.split(' ')

    digits = hand_str_to_digits(hand_str)
    hand_type = digits_to_type(jokerized_digits(digits))

    return Hand(bid=int(bid_str), digits=digits, type=hand_type)

# comparator function for two hands
def hand_cmp(h1, h2):
    if h1.type.value != h2.type.value:
        # hand type comparison
        return h1.type.value - h2.type.value
    
    else:
        # digit comparison 
        h1d = h1.digits
        h2d = h2.digits
        return (h1d > h2d) - (h1d < h2d)

with open('./input.txt', 'r') as file:
    lines = file.readlines()

hands = [line_to_hand(line) for line in lines]
sorted_hands = sorted(hands, key=cmp_to_key(hand_cmp))

total_score = 0
for i, hand in enumerate(sorted_hands):
    rank = i + 1
    score = hand.bid * rank
    total_score += score
    
print(total_score)
