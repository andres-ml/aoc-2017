import math

input = 312051
# input = 9

def coords(number) :
    base = int(math.sqrt(number))
    if base != math.sqrt(number) :
        base += 2 if base % 2 != 0 else 1

    start = math.pow(base - 2, 2) + 1

    coords = [base//2, -(base//2)+1]
    direction = [0, 1]
    current = start

    while current < number:
        current += 1
        coords[0] += direction[0]
        coords[1] += direction[1]

        if current == start + base - 2:
            direction = (-1, 0)
        elif current == start + base - 2 + (base - 1):
            direction = (0, -1)
        elif current == start + base - 2 + 2* (base - 1):
            direction = (1, 0)

    return coords

def first(coords) :
    manhattan = lambda coords: abs(coords[0]) + abs(coords[1])
    return manhattan(coords)

print(coords(input))