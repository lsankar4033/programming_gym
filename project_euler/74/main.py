from math import factorial

fs = [factorial(i) for i in range(10)]

def fac_sum(n):
    # factorial sum of digits
    digits = [int(d) for d in str(n)]

    return sum(fs[d] for d in digits)

def chain_length(n):
    # get the longest non-repeating chain starting with n
    seen = set([n])
    chain_length = 1

    while True:
        n = fac_sum(n)
        if n in seen:
            return chain_length
        seen.add(n)
        chain_length += 1

count = 0
for n in range(1, 1_000_000):
    if chain_length(n) == 60:
        count += 1
        print(n)

print("final count: ", count)