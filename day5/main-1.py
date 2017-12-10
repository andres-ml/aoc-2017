import sys

jumps = list(map(lambda line: int(line), sys.stdin.read().splitlines()))

position = 0
steps = 0

while position >= 0 and position < len(jumps):
    jumps[position] += 1
    position += jumps[position] - 1
    steps += 1

print(steps)
