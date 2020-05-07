from collections import defaultdict
from typing import List, Set, NamedTuple


class Hand():
    ...


def comp(a, b):
    return (a > b) - (a < b)


class HighCard(Hand, NamedTuple):
    cards: List[int]

    def compare(self, other):
        return comp(self.cards, other.cards)


class Pair(Hand, NamedTuple):
    pair: int
    others: List[int]

    def compare(self, other):
        if comp(self.pair, other.pair) != 0:
            return comp(self.pair, other.pair)

        return comp(self.others, other.others)


class TwoPair(Hand, NamedTuple):
    pair1: int
    pair2: int
    other: int

    def compare(self, other):
        if comp(self.pair1, other.pair1) != 0:
            return comp(self.pair1, other.pair1)

        if comp(self.pair2, other.pair2) != 0:
            return comp(self.pair2, other.pair2)

        return comp(self.other, other.other)


class Trip(Hand, NamedTuple):
    trip: int
    others: List[int]

    def compare(self, other):
        if comp(self.trip, other.trip) != 0:
            return comp(self.trip, other.trip)

        return comp(self.others, other.others)


class Straight(Hand, NamedTuple):
    high: int

    def compare(self, other):
        return comp(self.high, other.high)


class Flush(Hand, NamedTuple):
    cards: List[int]

    def compare(self, other):
        return comp(self.cards, other.cards)


class FullHouse(Hand, NamedTuple):
    trip: int
    pair: int

    def compare(self, other):
        if comp(self.trip, other.trip) != 0:
            return comp(self.trip, other.trip)

        return comp(self.pair, other.pair)


class Quad(Hand, NamedTuple):
    quad: int
    other: int

    def compare(self, other):
        if comp(self.quad, other.quad) != 0:
            return comp(self.quad, other.quad)

        return comp(self.other, other.other)


class StraightFlush(Hand, NamedTuple):
    high: int

    def compare(self, other):
        return comp(self.high, other.high)


def card_to_rank(c):
    rank_char = c[0]
    if rank_char == 'A':
        return 14
    elif rank_char == 'K':
        return 13
    elif rank_char == 'Q':
        return 12
    elif rank_char == 'J':
        return 11
    elif rank_char == 'T':
        return 10
    else:
        return int(rank_char)


def get_hand(cards: List[str]) -> Hand:
    rank_suit_cards = [(card_to_rank(c), c[1]) for c in cards]

    r = [c[0] for c in rank_suit_cards]
    rsorted = sorted(r)
    rrsorted = rsorted[::-1]
    is_straight = rsorted == list(range(rsorted[0], rsorted[-1] + 1))

    c = [c[1] for c in cards]
    is_flush = len(set(c)) == 1

    if is_straight and is_flush:
        return StraightFlush(rsorted[-1])

    rank_to_count = defaultdict(lambda: 0)
    for rank in r:
        rank_to_count[rank] += 1

    count_to_ranks = defaultdict(list)
    for rank, count in rank_to_count.items():
        count_to_ranks[count].append(rank)

    if 4 in count_to_ranks:
        return Quad(count_to_ranks[4][0], count_to_ranks[1][0])

    elif 3 in count_to_ranks and 2 in count_to_ranks:
        return FullHouse(count_to_ranks[3][0], count_to_ranks[2][0])

    elif is_flush:
        return Flush(rrsorted)

    elif is_straight:
        return Straight(rsorted[-1])

    elif 3 in count_to_ranks:
        trip_rank = count_to_ranks[3][0]
        others = [rank for rank in rrsorted if rank != trip_rank]
        return Trip(trip_rank, others)

    elif 2 in count_to_ranks and len(count_to_ranks[2]) == 2:
        pr2, pr1 = sorted(count_to_ranks[2])
        others = [rank for rank in rrsorted if rank != pr1 and rank != pr2]
        return TwoPair(pr1, pr2, others[0])

    elif 2 in count_to_ranks:
        pair_rank = count_to_ranks[2][0]
        others = [rank for rank in rrsorted if rank != pair_rank]
        return Pair(pair_rank, others)

    else:
        return HighCard(rrsorted)


def get_hand_rank(h: Hand):
    if isinstance(h, StraightFlush):
        return 8
    elif isinstance(h, Quad):
        return 7
    elif isinstance(h, FullHouse):
        return 6
    elif isinstance(h, Flush):
        return 5
    elif isinstance(h, Straight):
        return 4
    elif isinstance(h, Trip):
        return 3
    elif isinstance(h, TwoPair):
        return 2
    elif isinstance(h, Pair):
        return 1
    elif isinstance(h, HighCard):
        return 0

    else:
        raise ValueError(f'Unrecognized hand type: {type(h)}')


def compare_hands(h1: Hand, h2: Hand):
    hr1 = get_hand_rank(h1)
    hr2 = get_hand_rank(h2)
    if comp(hr1, hr2) != 0:
        return comp(hr1, hr2)

    return h1.compare(h2)


def games_from_file(file):
    games = []
    with open(file, 'r') as f:
        for line in f.readlines():
            all_cards = line.strip().split(' ')
            if len(all_cards) != 10:
                raise ValueError(f'found line with incorrect card count: {line.strip()}')

            games.append((all_cards[0:5], all_cards[5:]))

    return games


POKER_FILENAME = 'poker.txt'

if __name__ == '__main__':
    p1_count = 0
    games = games_from_file(POKER_FILENAME)
    for p1, p2 in games:
        if compare_hands(get_hand(p1), get_hand(p2)) == 1:
            p1_count += 1

        elif compare_hands(get_hand(p1), get_hand(p2)) == 0:
            print(f'Received equal hand game! {(p1, p2)}')

    print(p1_count)
