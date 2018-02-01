from collections import defaultdict

def get_counts(lst):
    counts = defaultdict(lambda : 0)
    for x in lst:
        counts[x] += 1

    return counts

def get_missing_numbers(a, b):
    a_counts = get_counts(a)
    b_counts = get_counts(b)

    missing_counts = {}
    for x, n in b_counts.items():
        missing_counts[x] = b_counts[x] - a_counts[x]

    missing_nums = []
    for x, n in sorted(missing_counts.items()):
        for i in range(n):
            missing_nums.append(x)

    return missing_nums

if __name__ == "__main__":
    int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    int(input().strip())
    b = list(map(int, input().strip().split(' ')))

    m = get_missing_numbers(a, b)
    print (" ".join(map(str, m)))
