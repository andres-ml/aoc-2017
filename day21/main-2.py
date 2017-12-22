import sys
import re
import itertools
import math

def read(line):
    to_matrix = lambda l: [list(r) for r in l.split('/')]
    return tuple(map(to_matrix, re.findall("[#./]+", line)))
    
# matrix print
def mprint(m):
    print('\n'.join( ''.join(r) for r in m ))
    print()

rules = [read(line) for line in sys.stdin.read().splitlines()]

def subSquare(m, i, j, size):
    return [ [m[i+x][j+y] for y in range(size)] for x in range(size) ]

def split(art):
    N = len(art)
    size = 2 if N % 2 == 0 else 3
    return [subSquare(art, i, j, size) for i in range(0, N, size) for j in range(0, N, size)]

def matches(input, art):
    return any(t == input for t in transforms(art))

def transforms(art):
    for _ in range(4):
        yield art
        yield flipx(art)
        yield flipy(art)
        art = rotate(art)
        
def rotate(m):
    N = len(m)
    return [ [m[N-j-1][i] for j in range(N)] for i in range(N)]
    
def flipx(m):
    N = len(m)
    return [ [m[i][N-j-1] for j in range(N)] for i in range(N)]
    
def flipy(m):
    N = len(m)
    return [ [m[N-i-1][j] for j in range(N)] for i in range(N)]
    
def expand(art):
    return next(output for input,output in rules if matches(input, art))
    
def combine(pieces):
    N = int(math.sqrt(len(pieces)))
    L = len(pieces[0])
    def get(i, j):
        ii, jj = i // L, j // L
        p = ii*N + jj
        x, y = i % L, j % L
        return pieces[p][x][y]
    return [[get(i,j) for j in range(N*L)] for i in range(N*L)]

def draw(loops):
    art = [list('.#.'), list('..#'), list('###')]
    for _ in range(loops):
        mprint(art)
        art = combine([expand(part) for part in split(art)])
    
    mprint(art)
    return art
    
result = draw(5)
print(sum(1 for row in result for x in row if x == '#'))


