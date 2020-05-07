def is_palindrome(s):
    return s == s[::-1]


if __name__ == '__main__':

    s = 0
    for n in range(1_000_000):
        ns = str(n)
        bns = bin(n)[2:]

        if is_palindrome(ns) and is_palindrome(bns):
            s += n

    print(s)
