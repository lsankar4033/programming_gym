
def diffs(seq):
    return [j-i for i, j in zip(seq[:-1], seq[1:])]


def next_in_seq(seq):
    diff_triangle = [seq]
    cur = seq
    while True:
        cur = diffs(cur)
        diff_triangle.append(cur)

        # if all elements in cur are 0, break!
        if all([c == 0 for c in cur]):
            break

    # move backwards up the triangle to get next in first arr
    next_inc = 0
    for diff in list(reversed(diff_triangle))[1:]:
        next_inc = diff[-1] + next_inc

    return next_inc


with open('./input.txt', 'r') as file:
    lines = file.readlines()

seqs = [[int(c.strip()) for c in line.split(' ')] for line in lines]

print(sum([next_in_seq(seq) for seq in seqs]))
