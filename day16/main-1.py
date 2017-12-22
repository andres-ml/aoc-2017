import sys
import re
from functools import reduce

input = sys.stdin.read()
moves = input.split(',')

programs = list('abcdefghijklmnop')

def dance(move):
    global programs
    if move[0] == 's':
        X = int(move[1:])
        programs = programs[-X:] + programs[:-X]
    elif move[0] == 'x':
        A, B = map(int, move[1:].split('/'))
        programs[A], programs[B] = programs[B], programs[A]
    elif move[0] == 'p':
        A, B = (programs.index(c) for c in move[1:].split('/'))
        programs[A], programs[B] = programs[B], programs[A]

for move in moves:
    dance(move)

print(''.join(programs))
