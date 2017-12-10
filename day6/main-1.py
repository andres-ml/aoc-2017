import sys

blocks = [int(x) for x in sys.stdin.read().splitlines()[0].split(' ')]
N = len(blocks)


def serialize(_blocks):
    result = []
    for i in range(N):
        result.append(str(i) + str(_blocks[i]))
    return ','.join(result)

cycles = 0
cache = []

while not (serialize(blocks) in cache):
    cache.append(serialize(blocks))
    index = next( (i for i in range(N) if blocks[i] == max(blocks)) )
    to_distribute = blocks[index]
    blocks[index] = 0
    while to_distribute > 0:
        index = (index + 1) % N
        blocks[index] += 1
        to_distribute -= 1
    cycles += 1

print(cycles)