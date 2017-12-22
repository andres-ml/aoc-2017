import sys
import re
from functools import reduce

input   = 'flqrgnkx'

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

hashes = [knot(input + '-' + str(i)) for i in range(128)]
char2bin = lambda c : bin(int(c, 16))[2:].zfill(4)
grid = [''.join([char2bin(c) for c in list(hash)]) for hash in hashes]

print(sum(sum(map(int,row)) for row in grid))

