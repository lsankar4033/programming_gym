from src.main import arith_seqs_3, perm_sets


def test_perm_sets():
    assert dict(perm_sets(10, 40)) == {
        '11': set([11]),
        '13': set([13, 31]),
        '17': set([17]),
        '19': set([19]),
        '23': set([23]),
        '29': set([29]),
        '37': set([37])
    }


def test_arith_seqs_3():
    ns = set([1, 3, 4, 5, 7, 8, 9])
    assert arith_seqs_3(ns) == [
        [1, 3, 5],
        [1, 4, 7],
        [1, 5, 9],
        [3, 4, 5],
        [3, 5, 7],
        [5, 7, 9],
        [7, 8, 9]
    ]
