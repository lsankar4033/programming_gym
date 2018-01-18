# Problem here: https://leetcode.com/problems/sentence-screen-fitting/#/description
# Start time 11:27
# Stop time 11:46

# NOTE: Below isn't fast enough...
def num_sentences(sentence, rows, cols):
    word_lengths = [len(w) for w in sentence]
    if any(l > cols for l in word_lengths):
        return 0

    num_sentences_so_far = 0
    cur_word = 0
    for _ in range(rows):
        col = 0

        while (col + word_lengths[cur_word] <= cols):
            col += word_lengths[cur_word] + 1
            cur_word += 1
            if cur_word == len(word_lengths):
                cur_word = 0
                num_sentences_so_far += 1

    return num_sentences_so_far
