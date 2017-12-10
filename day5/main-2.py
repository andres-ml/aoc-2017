import sys

jumps = list(map(lambda line: int(line), sys.stdin.read().splitlines()))

position = 0
steps = 0

while position >= 0 and position < len(jumps):
    original = position
    position += jumps[position]
    jumps[original] += 1 if jumps[original] < 3 else -1
    steps += 1

print(steps)
