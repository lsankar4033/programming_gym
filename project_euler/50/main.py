from math import sqrt

def sieve(n):
    r = [True] * n
    r[0] = r[1] = False
    r[4::2] = [False] * len(r[4::2])
    for i in range(int(1 + sqrt(n))):
        if r[i]:
            r[3*i::2*i] = [False] * len(r[3*i::2*i])

    return [i for i, v in enumerate(r) if v]

primes = sieve(1_000_000)

# length of the consecutive prime sum
length = 0

# value of the consecutive prime sum
largest = 0

# max value of the j variable(second for loop)
lastj = len(primes)

# two for loops
for i in range(len(primes)):
    for j in range(i+length, lastj):
        sol = sum(primes[i:j])
        if sol < 1000000:
            if sol in primes:
                length = j-i
                largest = sol
        else:
            lastj = j+1
            break

# printing the requried solution
print(largest)
