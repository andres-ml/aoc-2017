import sys
import re
import itertools

lines = sys.stdin.read().splitlines()
map = {}

for i in range(len(lines)):
    line = lines[i]
    for j in range(len(line)):
        map[(i,j)] = line[j] == '#'
        
class Virus :
    def __init__(self, x, y):
        self.pos = [x, y]
        self.dir = [-1, 0]
        self.infections = 0
        
    def burst(self):
        self.turn()
        self.infect()
        self.move()
        
    def turn(self):
        factor = 1 if infected(tuple(self.pos)) else -1
        self.dir = [self.dir[1]*factor, -self.dir[0]*factor]
        
    def infect(self):
        status = infected(tuple(self.pos))
        map[tuple(self.pos)] = not status
        if not status:
            self.infections += 1
        
    def move(self):
        self.pos[0] += self.dir[0]
        self.pos[1] += self.dir[1]
                
    def log(self):
        print('total infections:', self.infections)
        
infected = lambda c: c in map and map[c]

middle = len(lines) // 2
virus = Virus(middle, middle)

N = 10000
for _ in range(N):
    virus.burst()
    show(15)
    
virus.log()


