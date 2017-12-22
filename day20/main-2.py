import sys
import re

def read(line):
    matches = re.findall(r"(\w)=<(-?\d+,-?\d+,-?\d+)>", line)
    return {c:tuple(map(int, vector.split(','))) for c, vector in matches}

particles = [read(line) for line in sys.stdin.read().splitlines()]

csum = lambda l: list(map(sum, zip(*l)))

def move(particle):
    particle['v'] = csum([particle['v'], particle['a']])
    particle['p'] = csum([particle['p'], particle['v']])
    return particle
    
def dist(p1, p2):
    return sum( abs(a-b) for a,b in zip(p1['p'], p2['p']) )
    
def colliding(p1, p2):
    return dist(p1, p2) == 0

def closingIn(p1, p2):
    return dist(p1, p2) > dist(move(p1), move(p2))

t = 0
while True:
    for p in particles:
        move(p)
        
    particles = [p for p in particles if not any(colliding(p, x) for x in particles if x != p)]
    t += 1
    print(t, len(particles)) # ctrl+c once it stops changing :D
    
