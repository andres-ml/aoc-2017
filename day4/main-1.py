import sys

passphrases = list(sys.stdin.read().splitlines())

def no_repeats(items):
    if len(items) == 1:
        return True

    return len([x for x in items[1:] if x == items[0]]) == 0 and no_repeats(items[1:])

valid = (p for p in filter(lambda phrase : no_repeats(phrase.split(' ')), passphrases))
print(sum((1 for _ in valid)))