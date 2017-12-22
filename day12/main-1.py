import sys
import re
from functools import reduce

read = lambda line : [int(n) for n in re.findall(r"\d+", line)[1:]]
connections = [read(line) for line in sys.stdin.read().splitlines()]

def find(index, visited=set()) :
    if index in visited :
        return set([index])
    visited.add(index)
    return reduce(lambda carry, u: carry.union(u), [find(conn) for conn in connections[index]], visited)

print(len(find(0)))