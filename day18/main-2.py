import sys
import re
from pprint import pprint

def read(line):
    op, *params = re.findall(r"(?:\w|-?\d)+", line)
    return {'op': op, 'params': params}

instructions = [read(line) for line in sys.stdin.read().splitlines()]

class Program:
    def __init__(self, id):
        self.id = id
        self.ip = 0
        self.registers = {c:0 for c in 'abcdefghijklmnop'}
        self.registers['p'] = id
        self.queue = []
        self.count = 0
        
    def execute(self):
        if self.ip < 0 or self.ip >= len(instructions):
            return 0    # out of bounds
            
        instruction = instructions[self.ip]
        offset = getattr(self, instruction['op'])(*instruction['params'])
        self.ip += 1 if offset is None else offset
        return offset

    def get(self, val):
        return self.registers[val] if val in self.registers else int(val)

    def mul(self, destination, target):
        self.registers[destination] = self.get(destination) * self.get(target)
        
    def mod(self, destination, target):
        self.registers[destination] = self.get(destination) % self.get(target)
        
    def add(self, destination, target):
        self.registers[destination] = self.get(target) + self.get(destination)

    def set(self, destination, target):
        self.registers[destination] = self.get(target)

    def jgz(self, target, offset):
        if self.get(target) > 0:
            return self.get(offset)
            
    def snd(self, target):
        self.queue.append(self.get(target))

    def rcv(self, destination):
        val = self.buddy.send()
        if val is not None:
            self.registers[destination] = val
        else:
            return 0    # wait
            
    def send(self):
        if len(self.queue) > 0:
            self.count += 1
            return self.queue.pop(0)
        
        return None

def execute():
    p0 = Program(0)
    p1 = Program(1)
    p0.buddy = p1
    p1.buddy = p0
    
    loops = 0
    o0 = o1 = None
    while o0 != 0 or o1 != 0:   # wait for deadlock or both out of bounds
        o0 = p0.execute()
        o1 = p1.execute()
        loops += 1
        
    print('end. loops:', loops, 'p0 count:', p0.count, 'p1 count:', p1.count)
    
print(execute())
