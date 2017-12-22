import sys
import re
import itertools

def read(line):
    matches = re.findall(r"(\w)=<(-?\d+,-?\d+,-?\d+)>", line)
    return {c:tuple(map(int, vector.split(','))) for c, vector in matches}

particles = [{'index':i, 'particle': read(line)} for i, line in zip(itertools.count(), sys.stdin.read().splitlines())]

print(sorted(particles, key=lambda x: sum( map(abs, x['particle']['a']) ))[0])

