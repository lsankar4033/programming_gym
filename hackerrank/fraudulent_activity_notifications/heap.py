# TODO move this to the run.py

import operator

class Heap:
    # NOTE for testing
    def build_heap(is_max, lst):
        h = Heap(is_max)
        for n in lst:
            h.insert(n)
        return h

    def __init__(self, is_max):
        self.nodes = [] # The indexing on this list is reversed, so that the min/max exists in the *last* index
        self.cmp_fn = operator.gt if is_max else operator.lt

    # Switch between the two index spaces. This is necessary because of the list datastructure we use
    def idx_cnv(self, i):
        return len(self.nodes) - 1 - i

    def get_child_indices(self, i):
        i2 = self.idx_cnv(i)

        # children = i * 2 + 1, i * 2 + 2
        return [self.idx_cnv(c) for c in (i2 * 2 + 1, i2 * 2 + 2) if c < len(self.nodes)]

    # swap nodes at indices i1, i2
    def _swap(self, i1, i2):
        tmp = self.nodes[i1]
        self.nodes[i1] = self.nodes[i2]
        self.nodes[i2] = tmp

    # If idx specified should be swapped with one of its children, swap with one of them arbitrarily and
    # return the idx of the swapped child
    # If no swap is necessary, simply return the original idx
    def _attempt_swap(self, i):
        swappable_indices = [j for j in self.get_child_indices(i) if self.cmp_fn(self.nodes[j], self.nodes[i])]

        if len(swappable_indices) is 0:
            return i

        else:
            idx_to_swap = -1

            # TODO - clean this up...
            if len(swappable_indices) is 1:
                idx_to_swap = swappable_indices[0]
            else:
                (s0, s1) = swappable_indices # TODO generalize when non-binary heap
                idx_to_swap = s0 if self.cmp_fn(self.nodes[s0], self.nodes[s1]) else s1

            self._swap(idx_to_swap, i)
            return idx_to_swap

    # If either of i's children should be swapped with i, return True. False otherwise
    def _needs_swap(self, i):
        return any([self.cmp_fn(self.nodes[j], self.nodes[i]) for j in self.get_child_indices(i)])

    def _heapify(self, start_idx):
        cur_idx = start_idx
        while self._needs_swap(cur_idx):
            cur_idx = self._attempt_swap(cur_idx)

    # Hmm... somehow this doesn't quite work yet. I suspect a bug in the swapping logic
    def insert(self, n):
        self.nodes.append(n)
        self._heapify(len(self.nodes) - 1)

    # return the highest priority element
    def peek(self):
        return self.nodes[-1]

    def pop(self):
        if len(self.nodes) is 1:
            ret = self.nodes[0]
            self.nodes = []
            return ret

        else:
            root = self.nodes[-1]
            self._swap(0, -1)
            self.nodes = self.nodes[1:] # NOTE this may be non-performant

            self._heapify(len(self.nodes) - 1)

            return root

    # TODO doesn't quite work yet...
    # find and remove the element 'n'
    # currently, doesn't do anything if n doesn't exist in list (would probably want to raise ValueError)
    def delete(self, n):
        if n in self.nodes:
            ni = self.nodes.index(n)
            self._swap(ni, 0)
            self.nodes = self.nodes[1:] # NOTE this may be non-performant

            if len(self.nodes) > 1:
                self._heapify(ni - 1)

    def size(self):
        return len(self.nodes)

    # empty the heap into a lst in cmp_fn order
    def extract(self):
        ret = []
        while self.size() > 0:
            ret.append(self.pop())
        return ret
