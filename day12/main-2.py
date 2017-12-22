import sys
import re
from functools import reduce

read = lambda line : [int(n) for n in re.findall(r"\d+", line)[1:]]
connections = [read(line) for line in sys.stdin.read().splitlines()]

def find(index) :
    # wrap to allow multiple calls without reusing 'visited'
    def _find(index, visited=set()) :
        if index in visited :
            return set([index])
        visited.add(index)
        return reduce(lambda carry, u: carry.union(u), [_find(conn) for conn in connections[index]], visited)

    return _find(index)

groups = []
candidates = list(range(len(connections)))

while len(candidates) > 0:
    group = find(candidates[0])
    groups.append(group)
    candidates = [candidate for candidate in candidates if candidate not in group]

print(len(groups))