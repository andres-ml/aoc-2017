import sys
import re
sys.setrecursionlimit(3000)
input = sys.stdin.read()
# input = '<{o"i!a,<{i<a>'

def parse(index=0, end=None):
    score = 0
    while index < len(input):
        char = input[index]
        index += 1
        if char == end:
            break
        elif char == '<' and end != '>':
            child_score, index = parse(index, '>')
            score += child_score
        elif char == '{' and end != '>':
            child_score, index = parse(index, '}')
            score += child_score
        elif char == '!' and end == '>':
            index += 1
        elif end == '>' :
            score += 1

    return score, index

print(parse()[0])
