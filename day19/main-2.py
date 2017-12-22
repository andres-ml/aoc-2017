import sys
import re
from functools import reduce

map = [[c for c in line] for line in sys.stdin.read().splitlines()]

N = len(map)
M = len(map[0])

at = lambda p : map[p[0]][p[1]]
traversable = lambda p : at(p) != ' '

letters = ''
position = [-1, next(i for i in range(N) if traversable([0, i]))]
direction = [1, 0]

move = lambda p, d: [a + b for a, b in zip(p, d)]
fork = lambda x, y: [ [x, y], [y, x], [-y, -x] ]    # order is important

steps = 0
while direction is not None:
    position = move(position, direction)
    c = at(position)
    if not c in '|-+':
        letters += c
    direction = next((d for d in fork(*direction) if traversable(move(position, d))), None)
    steps += 1

print(letters, steps)
