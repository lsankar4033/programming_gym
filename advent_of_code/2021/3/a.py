with open('input.txt') as f:
    strs = [l.strip() for l in f.readlines()]

counts = []
for i in range(len(strs[0])):
    counts.append({
        '0': 0,
        '1': 0
    })

for s in strs:
    for i, c in enumerate(s):
        if c == '0':
            counts[i]['0'] += 1
        else:
            counts[i]['1'] += 1

# max key for each item in count joined is our num
max_bin = "".join([max(c, key=c.get) for c in counts])
min_bin = "".join([min(c, key=c.get) for c in counts])

print(int(max_bin, 2) * int(min_bin, 2))
