import sys
import re
import itertools

lines = sys.stdin.read().splitlines()
map = {}

for i in range(len(lines)):
    line = lines[i]
    for j in range(len(line)):
        map[(i,j)] = line[j]
        
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
        status = map.get(tuple(self.pos), '.')
        if status == '.':
            self.dir = [-self.dir[1], self.dir[0]]
        elif status == '#':
            self.dir = [self.dir[1], -self.dir[0]]
        elif status == 'F':
            self.dir = [-self.dir[0], -self.dir[1]]
        
    def infect(self):
        statuses = '.W#F'
        
        pos = tuple(self.pos)
        status = map.get(pos, '.')
        index = statuses.find(status)
        map[pos] = statuses[(index+1)%4]
        if map[pos] == '#':
            self.infections += 1
        
    def move(self):
        self.pos[0] += self.dir[0]
        self.pos[1] += self.dir[1]
                
    def log(self):
        print('total infections:', self.infections)
        
infected = lambda c: c in map and map[c] == '#'

middle = len(lines) // 2
virus = Virus(middle, middle)

def show(N=10):
    print(virus.pos)
    print('\n'.join((' '.join(map.get((i,j), '.') for j in range(-N//2, N+1)) for i in range(-N//2,N+1))))
    
N = 10000000
for _ in range(N):
    virus.burst()
    
virus.log()


