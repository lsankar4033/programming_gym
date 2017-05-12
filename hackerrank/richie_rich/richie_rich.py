# Problem here: https://www.hackerrank.com/challenges/richie-rich
import sys

# TODO: doesn't quite pass the test cases... getting frustrated so going to step away for a bit
# NOTE: might be easier to split into two phases:
# 1. convert to palindrome
# 2. maximize palindrome

def find_biggest_palindrome(num_str, n, k):
    front, back, mid = [], [], []
    if n % 2 == 0:
        front = list(num_str[:int(n/2)])
        back = list(num_str[int(n/2):][::-1])
    else:
        front = list(num_str[:int(n/2)])
        mid = [num_str[int(n/2)]]
        back = list(num_str[int(n/2)+1:][::-1])

    diff_w_9 = []
    diff_wo_9 = []
    same = []
    for i in range(len(front)):
        if front[i] != back[i] and front[i] != "9" and back[i] != "9":
            diff_wo_9.append(i)
        elif front[i] != back[i]:
            diff_w_9.append(i)
        elif front[i] != "9":
            same.append(i)

    if len(diff_w_9) + len(diff_wo_9) > k:
        return -1

    while k > 0:
        contenders = []
        if len(diff_w_9) > 0:
            contenders.append(diff_w_9[0])
        if len(diff_wo_9) > 0:
            contenders.append(diff_wo_9[0])
        if len(same) > 0:
            contenders.append(same[0])

        if len(contenders) == 0:
            break

        contenders.sort()
        found_contender = False
        for contender in contenders:
            requires_double = len(same) > 0 and same[0] == contender
            can_double = len(diff_wo_9) > 0 and diff_wo_9[0] == contender

            if requires_double and k > 1 and k > len(diff_w_9) + len(diff_wo_9):
                # record a same switch!
                found_contender = True
                front[same[0]] = "9"
                back[same[0]] = "9"
                k -= 2
                same = same[1:]

            elif requires_double:
                # we just need to move on from this same... can't mark found
                same = same[1:]

            elif can_double and k > 1 and k > len(diff_wo_9) + len(diff_wo_9):
                # do the double!
                found_contender = True
                front[diff_wo_9[0]] = "9"
                back[diff_wo_9[0]] = "9"
                k -= 2
                diff_wo_9 = diff_wo_9[1:]

            elif can_double:
                # do the single on the double
                found_contender = True
                new_digit = max(front[diff_wo_9[0]], back[diff_wo_9[0]])
                front[diff_wo_9[0]] = new_digit
                back[diff_wo_9[0]] = new_digit
                k -= 1
                diff_wo_9 = diff_wo_9[1:]

            else:
                # do the single on the single
                found_contender = True
                new_digit = max(front[diff_w_9[0]], back[diff_w_9[0]])
                front[diff_w_9[0]] = new_digit
                back[diff_w_9[0]] = new_digit
                k -= 1
                diff_w_9 = diff_w_9[1:]

            # one contender row at a time
            if found_contender:
                break

        # once no more contenders, break
        if not found_contender:
            break

    # At very end, if k still exists, change mid if we can!
    if k > 0 and len(mid) > 0:
        mid = ["9"]

    return "".join(front + mid + back[::-1])

"""
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
number = input().strip()

print(find_biggest_palindrome(number, n, k))
"""
