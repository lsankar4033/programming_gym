# Problem here: https://leetcode.com/problems/the-skyline-problem/#/description
# Started 10:15
# Paused 11:26
import heapq

from heapq import heapify, heappop, heappush
from itertools import chain

# Taken from https://stackoverflow.com/questions/10162679/python-delete-element-from-heap
def heapremove(h, i):
    h[i] = h[-1]
    h.pop()

    # O(n)
    heapify(h)

    # O(log(n))
    #heapq._siftup(h, i)
    #heapq._siftdown(h, 0, i)

def get_endpoint_heap(buildings):
    h = list(chain.from_iterable(([(b[0], b), (b[1], b)] for b in buildings)))
    heapify(h)
    return h

def remove_bldg_from_height_heap(bldg, height_heap):
    if len(height_heap) == 1:
        height_heap.pop()
    else:
        matching_i = next(i for (i, (_, b)) in enumerate(height_heap) if b is bldg)
        heapremove(height_heap, matching_i)

def get_base_skyline(endpoint_heap):
    height_heap = []
    skyline = []
    cur_height = 0
    while len(endpoint_heap) > 0:
        (endpoint, bldg) = heappop(endpoint_heap)

        if endpoint == bldg[0]:
            heappush(height_heap, (-1 * bldg[2], bldg))
        else:
            remove_bldg_from_height_heap(bldg, height_heap)

        if len(height_heap) == 0 and cur_height != 0:
            skyline.append([endpoint, 0])
            cur_height = 0
        elif height_heap[0] != cur_height:
            skyline.append([endpoint, height_heap[0][1][2]])
            cur_height = height_heap[0]

    return skyline

def get_skyline(buildings):
    endpoint_heap = get_endpoint_heap(buildings)
    skyline = get_base_skyline(endpoint_heap)
    return skyline
