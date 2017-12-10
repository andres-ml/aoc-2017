import sys
import re

input = '106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36'
N = 256

lengths = [int(n) for n in input.split(',')]

numbers = list(range(N))

current_position = 0
skip_size = 0

for length in lengths:
    start = current_position
    for i in range(length // 2):
        i1 = (start + i) % N
        i2 = (start + length - i - 1) % N
        numbers[i1], numbers[i2] = numbers[i2], numbers[i1]
    current_position += length + skip_size
    skip_size += 1



print(numbers[0]*numbers[1])