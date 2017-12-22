import sys
import re
from functools import reduce

input = 'jxqlasbh'

# day 10 func
def knot(string):
    N       = 256
    loops   = 64
    suffix  = [17, 31, 73, 47, 23]

    lengths = [ord(c) for c in string] + suffix
    numbers = list(range(N))

    current_position = 0
    skip_size = 0

    for _ in range(loops):
        for length in lengths:
            start = current_position
            # swap elements
            for i in range(length // 2):
                i1 = (start + i) % N
                i2 = (start + length - i - 1) % N
                numbers[i1], numbers[i2] = numbers[i2], numbers[i1]
            current_position += length + skip_size
            skip_size += 1

    dense_hash = [reduce(lambda carry, x: x^carry, numbers[i:i+16]) for i in range(0, N, 16)]

    return ''.join(hex(val)[2:].rjust(2, '0') for val in dense_hash)

# day 14

hashes = [knot(input + '-' + str(i)) for i in range(128)]
char2bin = lambda c : bin(int(c, 16))[2:].zfill(4)
grid = [[int(x) for x in ''.join([char2bin(c) for c in list(hash)])] for hash in hashes]

groups = {}
counter = 0

# grid = [row[:8] for row in grid[:8]]
N = len(grid)

serialize = lambda i, j: ','.join(map(str, [i, j]))

def adjacent(i, j):
    def _adjacent(i, j, visited=[]):
        result = []
        if (i,j) in visited or not (0 <= i < N and 0 <= j < N) or grid[i][j] != 1:
            return result
        visited.append((i, j))
        result.append((i, j))
        for ii, jj in [(0,1),(0,-1),(1,0),(-1,0)]:
            result += _adjacent(i+ii, j+jj)
        return result

    return _adjacent(i, j)


for i in range(N):
    for j in range(N):
        val = grid[i][j]
        serialized = serialize(i, j)
        if val == 1:
            group = next((groups[serialize(x, y)] for x, y in adjacent(i, j) if serialize(x, y) in groups), None)
            if group is not None:
                groups[serialized] = group
            else :
                groups[serialized] = counter
                counter += 1

print(counter)
# def pr(i):
#     return ''.join(str(groups[serialize(i,j)]) if grid[i][j] == 1 else '.' for j in range(N))
# print('\n'.join(pr(i) for i in range(N)))
