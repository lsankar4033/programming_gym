
from string import ascii_lowercase as ALPHABET


def caesar(message, offset):
    trans = str.maketrans(ALPHABET, ALPHABET[offset:] + ALPHABET[:offset])
    return message.lower().translate(trans)


print(caesar("vcab", -8))
print(caesar("jm", -8))
print(caesar("bpm", -8))
print(caesar("bzcbp", -8))
