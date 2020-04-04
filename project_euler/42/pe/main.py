LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_word_list():
    data = ""
    with open('words.txt', 'r') as r:
        data = r.read()

    data = data.strip().replace('"', '')
    return data.split(",")


def score(word):
    w2 = word.upper()
    return sum([LETTERS.index(c) + 1 for c in w2])


def tri_gen():
    n = 1
    while True:
        yield n * (n + 1) / 2
        n += 1


if __name__ == '__main__':
    words = get_word_list()

    scores = [score(w) for w in words]
    scores.sort()

    tri_g = tri_gen()

    count = 0
    cur_score_idx = 0
    cur_tri = next(tri_g)

    while cur_score_idx < len(scores):
        if scores[cur_score_idx] == cur_tri:
            print(f"Match at {cur_tri}")
            count += 1
            cur_score_idx += 1

        elif scores[cur_score_idx] < cur_tri:
            while cur_score_idx < len(scores) and scores[cur_score_idx] < cur_tri:
                cur_score_idx += 1

        else:
            while cur_tri < scores[cur_score_idx]:
                cur_tri = next(tri_g)

    print(f"Count: {count}")
