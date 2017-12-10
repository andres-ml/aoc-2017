import math

input = 312051
# input = 9

def serialize(coords) :
    return str(coords[0]) + ',' + str(coords[1])

def calculate(coords, vals) :
    result = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:
                pos = [coords[0]+i, coords[1]+j]
                serialized = serialize(pos)
                if serialized in vals:
                    result += vals[serialized]
    return result


def spiral():
    coords = [1, 0]
    vals = {"0,0":1}
    direction = [0, 0]
    base = 1
    while True:
        # decide if base change
        if len(vals) == math.pow(base, 2):
            print('spin')
            base += 2
            # coords[0] += 1
            direction = [0, 1]
            ltt = base - 2
        # calculate and yield
        val = calculate(coords, vals)
        vals[serialize(coords)] = val
        yield val
        # move
        coords[0] += direction[0]
        coords[1] += direction[1]

        ltt -= 1
        if ltt == 0:
            ltt = base - 1
            if direction[0] == 0 and direction[1] == 1:
                direction = [-1, 0]
            elif direction[0] == -1 and direction[1] == 0:
                direction = [0, -1]
            else :
                direction = [1, 0]



def solve(number):
    return next((x for x in spiral() if x > number))

print(solve(input))