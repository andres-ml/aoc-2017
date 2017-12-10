import sys
import re
from functools import reduce

input   = '106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36'
# input = '1,2,4'
N       = 256
loops   = 64
suffix  = [17, 31, 73, 47, 23]

lengths = [ord(c) for c in input] + suffix
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

print(''.join(hex(val)[2:].rjust(2, '0') for val in dense_hash))