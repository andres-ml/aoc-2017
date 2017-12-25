RIGHT = 1
LEFT = -1

cursor = 0
tape = {}

# manual input because lazy:
steps = 12481997
state = 'A'
states = {
    'A': {
        0: [1, RIGHT, 'B'],
        1: [0, LEFT, 'C']
    },
    'B': {
        0: [1, LEFT, 'A'],
        1: [1, RIGHT, 'D']
    },
    'C': {
        0: [0, LEFT, 'B'],
        1: [0, LEFT, 'E']
    },
    'D': {
        0: [1, RIGHT, 'A'],
        1: [0, RIGHT, 'B']
    },
    'E': {
        0: [1, LEFT, 'F'],
        1: [1, LEFT, 'C']
    },
    'F': {
        0: [1, RIGHT, 'D'],
        1: [1, RIGHT, 'A']
    },
}

for _ in range(steps):
    val = tape.get(cursor, 0)
    move = states[state][val]
    tape[cursor] = move[0]
    cursor += move[1]
    state = move[2]

print(sum(tape.values()))
