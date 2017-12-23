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

def execute():
    p = Program()

    while not p.finished:
        p.execute()

    print(p.count)

execute()