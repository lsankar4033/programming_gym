from src.main import *


def str_to_cards(s):
    return s.split(' ')


p11 = str_to_cards('5H 5C 6S 7S KD')
p12 = str_to_cards('5D 8C 9S JS AC')
p13 = str_to_cards('2D 9C AS AH AC')
p14 = str_to_cards('4D 6S 9H QH QC')
p15 = str_to_cards('2H 2D 4C 4D 4S')

p21 = str_to_cards('2C 3S 8S 8D TD')
p22 = str_to_cards('2C 5C 7D 8S QH')
p23 = str_to_cards('3D 6D 7D TD QD')
p24 = str_to_cards('3D 6D 7H QD QS')
p25 = str_to_cards('3C 3D 3S 9S 9D')

quad = str_to_cards('3C 3D 3S 3H 9D')
two_pair = str_to_cards('3D 6D 3S 6S QD')
straight_flush = str_to_cards('6D, 7D, 8D, 9D, TD')


def test_get_hand():
    assert get_hand(p11) == Pair(5, [13, 7, 6])
    assert get_hand(p12) == HighCard([14, 11, 9, 8, 5])
    assert get_hand(p13) == Trip(14, [9, 2])
    assert get_hand(p14) == Pair(12, [9, 6, 4])
    assert get_hand(p15) == FullHouse(4, 2)

    assert get_hand(p21) == Pair(8, [10, 3, 2])
    assert get_hand(p22) == HighCard([12, 8, 7, 5, 2])
    assert get_hand(p23) == Flush([12, 10, 7, 6, 3])
    assert get_hand(p24) == Pair(12, [7, 6, 3])
    assert get_hand(p25) == FullHouse(3, 9)

    assert get_hand(quad) == Quad(3, 9)
    assert get_hand(two_pair) == TwoPair(6, 3, 12)
    assert get_hand(straight_flush) == StraightFlush(10)


def test_compare_hands():
    assert compare_hands(get_hand(p11), get_hand(p21)) == -1
    assert compare_hands(get_hand(p12), get_hand(p22)) == 1
    assert compare_hands(get_hand(p13), get_hand(p23)) == -1
    assert compare_hands(get_hand(p14), get_hand(p24)) == 1
    assert compare_hands(get_hand(p15), get_hand(p25)) == 1
