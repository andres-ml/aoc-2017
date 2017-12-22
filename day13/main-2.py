import sys
import re
import itertools

layers = {}

for line in sys.stdin.read().splitlines():
    index, depth = map(int, re.findall(r"\d+", line))
    layers[index] = depth

caught      = lambda picosecond, delay: (picosecond + delay) % (layers[picosecond] * 2 - 2) == 0
clean_run   = lambda delay: all(not caught(index, delay) for index in layers.keys())

print(next(delay for delay in itertools.count() if clean_run(delay)))
