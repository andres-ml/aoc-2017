import sys
import re
from functools import reduce

input = sys.stdin.read()
offset = int(input)
loops = 2017


# offset = 3
# loops = 8

buffer = [0]
position = 0

for i in range(1, loops + 1):
    position = (position + offset) % len(buffer) + 1
    buffer = buffer[:position] + [i] + buffer[position:]

print(buffer[position + 1])