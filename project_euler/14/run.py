# Longest Collatz sequence
# Problem here: https://projecteuler.net/problem=14
# Naive approach: iterate down from 1000000, keeping track of highest seen Collatz number. Also keep
# track of all numbers seen on each sequence as we can skip these when we get to them.

def get_collatz_seq(i):
    cur = i
    ret = [cur]
    while cur != 1:
        if cur % 2 == 0:
            cur = cur / 2
        else:
            cur = 3 * cur + 1

        ret.append(cur)

    return ret

if __name__ == "__main__":
    visited = set()
    greatest_length = 0
    best_starting_num = None
    for i in range(999999, 1, -1):
        if i not in visited:
            collatz_seq = get_collatz_seq(i)
            visited |= set(collatz_seq)

            if len(collatz_seq) > greatest_length:
                greatest_length = len(collatz_seq)
                best_starting_num = i

    print("Longest collatz sequence found for {} of length {}".format(best_starting_num, greatest_length))
