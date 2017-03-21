# Challenge here: https://www.hackerrank.com/challenges/recursive-digit-sum
import sys

def get_digits(n):
    return [int(i) for i in list(str(n))]

def get_digit_sum(n):
    return sum(get_digits(n))

# NOTE - this method is just copied around in all hackerrank modules
def get_tuple_from_stdin():
    l = sys.stdin.readline().strip()
    return [int(i) for i in l.split(" ")]

if __name__ == "__main__":
    (n, k) = get_tuple_from_stdin()

    cur_n = get_digit_sum(n) * k
    while True:
        next_n = get_digit_sum(cur_n)

        if cur_n == next_n:
            break;

        cur_n = next_n

    print(cur_n)
