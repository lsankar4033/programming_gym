import unittest
from heap import *

class TestHeap(unittest.TestCase):

    # Not the most orthogonal unit testing...
    def test_max_heap(self):
        h = Heap.build_heap(True, [501, 4, 18, 5, 0, 1, 20])

        self.assertEqual(h.extract(),
                         [501, 20, 18, 5, 4, 1, 0])

    def test_min_heap(self):
        h = Heap.build_heap(False, [409, 12, 18, 0, 90, 83, 1])

        self.assertEqual(h.extract(),
                         [0, 1, 12, 18, 83, 90, 409])
