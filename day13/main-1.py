import sys
import re

layers = {}

for line in sys.stdin.read().splitlines():
    index, depth = map(int, re.findall(r"\d+", line))
    layers[index] = depth
    
severity = lambda index: index * layers[index]
caught = lambda picosecond: picosecond % (layers[picosecond] * 2 - 2) == 0
    
total = sum(severity(index) for index in layers.keys() if caught(index))

print(total)
