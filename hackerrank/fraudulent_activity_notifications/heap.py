# TODO move this to the run.py

import operator

class Heap:
    def __init__(self, is_max):
        self.nodes = [] # The indexing on this list is reversed, so that the min/max exists in the *last* index
        self.cmp_fn = operator.lt if is_max else operator.gt

    # Switch between the two index spaces. This is necessary because of the list datastructure we use
    def idx_cnv(self, i):
        return len(self.nodes) - 1 - i

    def get_child_indices(self, i):
        # Convert to other index space, do fancy base 2 operations...
        pass

    # If idx specified should be swapped with one of its children, swap with one of them arbitrarily and
    # return the idx of the swapped child
    # If no swap is necessary, simply return the original idx
    def _attempt_swap(self, i):
        swappable_indices = [j for j in self.get_child_indices(i) if self.cmp_fn(i, j)]

        if len(swappable_indices) is 0:
            return i

        else:
            idx_to_swap = swappable_indices[0]
            tmp = self.nodes[idx_to_swap]
            self.nodes[idx_to_swap] = self.nodes[i]
            self.nodes[i] = tmp
            return idx_to_swap

    # If either of i's children should be swapped with i, return True. False otherwise
    def _needs_switch(self, i):
        return any([self.cmp_fn(i, j) for j in self.get_child_indices(i)])

    def insert(self, n):
        self.nodes.append(n)

        # NOTE - this should be extracted into a method
        cur_idx = len(self.nodes) - 1
        while (self._needs_switch(cur_idx)):
            cur_idx = self._attempt_swap(cur_idx)

    def delete(self, n):
        # swap element with a leaf

        # delete element from end of list

        # swap leaf until we're stable
        pass

    def size(self):
        return len(self.nodes)
