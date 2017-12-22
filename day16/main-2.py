import sys
import re
from functools import reduce

input = sys.stdin.read()
loops = int(1e9)

moves = input.split(',')

programs = list('abcdefghijklmnop')

def dance(move, programs):
    if move[0] == 's':
        X = int(move[1:])
        programs = programs[-X:] + programs[:-X]
    elif move[0] == 'x':
        A, B = map(int, move[1:].split('/'))
        programs[A], programs[B] = programs[B], programs[A]
    elif move[0] == 'p':
        A, B = (programs.index(c) for c in move[1:].split('/'))
        programs[A], programs[B] = programs[B], programs[A]
    return programs

def perform(starting):
    result = starting
    for move in moves:
        result = dance(move, result)
    return result

def find_cycle(programs, loops):
    found = [programs]
    for i in range(loops):
        programs = perform(programs)
        found.append(programs)
        middle = len(found) // 2
        if found[:middle] == found[middle:]:
            return found[:middle]

cycle = find_cycle(programs, loops)
print(''.join(cycle[loops % len(cycle)]))