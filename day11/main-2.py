import sys
import re

input = sys.stdin.read().strip()
moves = input.split(',')

position = [0, 0]

def translate(move):
    if move == 'n':
        return [0, 1]
    elif move == 'ne':
        return [1, 0.5]
    elif move == 'se':
        return [1, -0.5]
    elif move == 's':
        return [0, -1]
    elif move == 'sw':
        return [-1, -0.5]
    elif move == 'nw':
        return [-1, 0.5]
    else :
        print("invalid move", move)
        exit(1)

# manhattan-like distance, but moving horizontally(x) also moves us vertically
def hex_distance(position):
    x = abs(position[0])
    y = max(0, abs(position[1]) - x / 2)
    return int(x + y)
        
furthest = 0

for move in moves:
    offset = translate(move)
    position[0] += offset[0]
    position[1] += offset[1]
    furthest = max(furthest, hex_distance(position))
    
print(furthest)
