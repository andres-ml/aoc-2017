import sys
import re
sys.setrecursionlimit(3000)
input = sys.stdin.read()
# input = '{{<!>},{<!>},{<!>},{<a>}}'

def parse(index=0, end=None, depth=0):
    score = depth
    while index < len(input):
        char = input[index]
        index += 1
        if char == end:
            break
        elif char == '<' and end != '>':
            _, index = parse(index, '>', depth + 1)
        elif char == '{' and end != '>':
            child_score, index = parse(index, '}', depth + 1)
            score += child_score
        elif char == '!' and end == '>':
            index += 1

    return score, index

print(parse()[0])
