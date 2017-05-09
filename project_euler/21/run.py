# Amicable numbers
# Problem here: https://projecteuler.net/problem=21
# Naive solution: Iterate through numbers up to 10000, generating divisor sums for each. Where amicable number
# pairs are found, add to a running sum of amicable numbers.

import math

def get_divisors(n):
    divisors = {1}
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors |= {i, n / i}

    return divisors

def get_divisor_sum(n):
    return sum(get_divisors(n))

if __name__ == "__main__":
    amicable_sum = 0
    divisor_sums = {}
    for i in range(10000):
        divisor_sums[i] = get_divisor_sum(i)

        dual_sum = divisor_sums[i]
        if dual_sum in divisor_sums and dual_sum != i and divisor_sums[dual_sum] == i:
            print("amicable pair found: {}, {}".format(i, dual_sum))
            amicable_sum += i + dual_sum

    print("Solution: {}".format(amicable_sum))
