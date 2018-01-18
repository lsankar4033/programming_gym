# Problem here: https://www.hackerrank.com/challenges/richie-rich
import sys

from collections import namedtuple

# TODO: The actual solution is to consider each digit in decreasing significance and do the best move on that
# digit that still leaves enough moves to minimally deal with the rest of the string. And if moves left over
# at end, deal with middle digit as well.

IntermediateState = namedtuple('IntermediateState', ['front', 'mid', 'back', 'moves_left'])

def _state_to_num(state):
    return "".join(state.front + state.mid + state.back[::-1])

def _build_init_state(num_str, n, k):
    front, back, mid = [], [], []
    if n % 2 == 0:
        front = list(num_str[:int(n/2)])
        back = list(num_str[int(n/2):][::-1])
    else:
        front = list(num_str[:int(n/2)])
        mid = [num_str[int(n/2)]]
        back = list(num_str[int(n/2)+1:][::-1])

    return IntermediateState(front, mid, back, k)

def _convert_to_palindrome(state):


    return state

def _maximize_palindrome(state):
    return state

def find_biggest_palindrome(num_str, k):
    state = _build_init_state(num_str, len(num_str), k)
    print("Initial state: {}".format(state))

    num_diff = 0
    for i in range(len(state.front)):
        if state.front[i] != state.back[i]:
            num_diff += 1
    if state.moves_left < num_diff:
        return -1

    state = _convert_to_palindrome(state)
    print("Palindrome state: {}".format(state))

    state = _maximize_palindrome(state)
    print("Maximized state: {}".format(state))

    return _state_to_num(state)

"""
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
number = input().strip()

print(find_biggest_palindrome(number, k))
"""
