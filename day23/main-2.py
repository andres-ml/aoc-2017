import sys
import re
from pprint import pprint

def read(line):
    op, *params = re.findall(r"(?:\w|-?\d)+", line)
    return {'op': op, 'params': params}

instructions = [read(line) for line in sys.stdin.read().splitlines()]

class Program:
    def __init__(self):
        self.ip = 0
        self.registers = {c:0 for c in 'abcdefgh'}
        self.registers['a'] = 1
        self.count = {}
        self.finished = False

    def execute(self):
        if self.ip < 0 or self.ip >= len(instructions):
            self.finished = True
            return

        instruction = instructions[self.ip]
        offset = getattr(self, instruction['op'])(*instruction['params'])
        self.ip += 1 if offset is None else offset

        self.count[instruction['op']] = self.count.get(instruction['op'], 0) + 1

        return offset

    def get(self, val):
        return self.registers[val] if val in self.registers else int(val)

    def mul(self, destination, target):
        self.registers[destination] = self.get(destination) * self.get(target)

    def sub(self, destination, target):
        self.registers[destination] = self.get(destination) - self.get(target)

    def set(self, destination, target):
        self.registers[destination] = self.get(target)

    def jnz(self, target, offset):
        if self.get(target) != 0:
            return self.get(offset)

p = Program()

# initialize
for _ in range(8):
    p.execute()

h = 0
# outer loop, exit condition is b == c and b increases by 17 every loop (inst. 31)
for i in range(p.registers['b'], p.registers['c'] + 1, 17):
    # h is increased by 1 if f is 0;
    # f is set to 0 if exists x€[2..b] | b % x == 0 (inst. 14-15)
    f = 1
    for j in range(2, i):
        if i % j == 0:
            f = 0
            break # the 2 innermost never set f to 1 once it's set to 0
    if f == 0:
        h += 1

print(h)
