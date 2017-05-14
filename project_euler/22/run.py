import string

f = open('./names.txt')
names = [quoted_name[1:-1] for quoted_name in f.readline().split(",")]
names.sort()

total_score = 0
for (i, name) in enumerate(names):
    # i + 1 is what we want
    char_scores = [string.ascii_lowercase.index(c.lower()) + 1 for c in name]
    total_score += (i + 1) * sum(char_scores)

print(total_score)
