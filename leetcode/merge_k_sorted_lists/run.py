# Problem here: https://leetcode.com/problems/merge-k-sorted-lists/#/description
# Time taken: 48 minutes
from heapq import heappush, heappop, heapify

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Comparison operators used in heap
    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return self.val != other.val

# NOTE: utility function!
def arr_to_list(arr):
    if len(arr) == 0:
        return None

    root = ListNode(arr[0])
    cur_node = root
    for v in arr[1:]:
        new_node = ListNode(v)
        cur_node.next = new_node
        cur_node = new_node

    return root

# NOTE: utility function!
def list_to_arr(lst):
    ret = []
    next_node = lst
    while next_node is not None:
        ret.append(next_node.val)
        next_node = next_node.next

    return ret

def merge(lists):
    min_heap = [n for n in lists if n]
    heapify(min_heap)

    phantom_root = ListNode(-1)
    cur = phantom_root
    sorted_list = []
    num_empty = 0
    while num_empty < len(lists):
        next_node = heappop(min_heap)
        new_node = ListNode(next_node.val)
        cur.next = new_node
        cur = new_node

        if next_node.next is not None:
            heappush(min_heap, next_node.next)
        else:
            num_empty += 1

    while len(min_heap) > 0:
        node = heappop(min_heap)
        sorted_list.append(node.val)

    return phantom_root.next
