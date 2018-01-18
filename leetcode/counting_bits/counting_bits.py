# Problem here: https://leetcode.com/problems/counting-bits/#/description
# Time taken: 10 minutes (puzzled about algorithm for a bit)

# Counts bits in all numbers 0 -> num
def count_bits(num):
    res = [0]
    while len(res) <= num:
        res += [i + 1 for i in res]
    return res[:num+1]
