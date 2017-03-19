
def p(n):
    a = [True] * n
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for x in xrange(i * i, n, i):
                a[x] = False

if __name__ == "__main__":
    print sum(p(2 * 1000 * 1000))
