import math


def truncate(n, left=True):
    sn = str(n)
    if len(sn) == 1:
        return None

    tsn = sn[1:] if left else sn[0:-1]
    return int(tsn)


def truncations(n):
    truncs = set([n])

    next_n = truncate(n, True)
    while next_n is not None:
        truncs.add(next_n)
        next_n = truncate(next_n, True)

    next_n = truncate(n, False)
    while next_n is not None:
        truncs.add(next_n)
        next_n = truncate(next_n, False)

    return truncs


def check_prime(n, prime_map={}):
    if n == 1:
        return False

    if n in prime_map:
        return prime_map[n]

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def find_all_truncatable():
    prime_map = {}
    truncatable = []
    cur = 10
    num_found = 0
    while num_found < 11:
        ts = truncations(cur)

        composite = False
        for t in ts:
            p = check_prime(t, prime_map)
            prime_map[t] = p

            if not p:
                composite = True
                break

        if not composite:
            print(f'Found: {cur}')
            truncatable.append(cur)
            num_found += 1

        cur += 1

    print(f'Truncatable: {truncatable}')
    print(f'Sum: {sum(truncatable)}')


if __name__ == '__main__':
    find_all_truncatable()
