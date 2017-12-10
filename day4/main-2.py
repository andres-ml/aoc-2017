import sys
import itertools

passphrases = list(sys.stdin.read().splitlines())

def valid(items):
    if len(items) == 1:
        return True

    anagrams = [''.join(letters) for letters in itertools.permutations(items[0])]

    return len([x for x in items[1:] if x in anagrams]) == 0 and valid(items[1:])

passing = (p for p in filter(lambda phrase : valid(phrase.split(' ')), passphrases))
print(sum((1 for _ in passing)))