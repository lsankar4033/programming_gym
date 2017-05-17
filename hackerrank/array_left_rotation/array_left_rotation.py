(n, k) = [int(c) for c in input().split(" ")]
lst = input().split(" ")

reduced_k = k % n
new_lst = lst[reduced_k:] + lst[0:reduced_k]

print(" ".join(new_lst))
