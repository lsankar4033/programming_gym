# Challenge here: https://www.hackerrank.com/challenges/fraudulent-activity-notifications

# FANCY SOLUTION
# A sophisticated solution involves keeping two heaps, a maxheap for the smaller half of elements and a
# minheap for the larger half. When we encounter a new element, determine which side to put it into by looking
# at the min/max of the heaps and then insert. If necessary, balance the queues afterwards by popping/pushing.
# The median can be calculated by looking at the max/min of the heap with the larger # of elements or the
# average of the max/min if both have the same number of elements.
# This algorithm will keep track of the median of all elements seen so far. To keep track of the last d, we
# can keep a list of pointers to specific points in the heap of elements we've seen so far (stack of
# pointers). Every time we add a new element, we first have to do some magic that involves heap implementation
# details... I'll first try a naive solution

# NAIVE SOLUTION - TRY FIRST
# Keep track of the last d elements in a queue and repeatedly remove the last element and do a sort on the
# remaining elements. This will take O(n * dlog(d)) time...
import sys

from statistics import median

# NOTE - this method is just copied around in all hackerrank modules
def get_tuple_from_stdin():
    l = sys.stdin.readline().strip()
    return [int(i) for i in l.split(" ")]

# start with naive solution
def get_num_notifications(expenditures, d):

    # iterate through all slices of length d and compare median with next elt
    # (use median fn from statistics module)


    pass

if __name__ == "__main__":

    #get_tuple_from_stdin()
    pass
