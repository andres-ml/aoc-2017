import sys
import re
from pprint import pprint

def read(line):
    op, *params = re.findall(r"(?:\w|-?\d)+", line)
    return {'op': op, 'params': params}

instructions    = [read(line) for line in sys.stdin.read().splitlines()]
registers       = {c:0 for c in 'abcdefghijklmonpqrstu'}

ip = 0
sounds = []

def get(val):
    return registers[val] if val in registers else int(val)

def mul(destination, target):
    registers[destination] = get(destination) * get(target)
    
def mod(destination, target):
    registers[destination] = get(destination) % get(target)
    
def add(destination, target):
    registers[destination] = get(target) + get(destination)

def set(destination, target):
    registers[destination] = get(target)
    
def snd(target):
    sounds.append(get(target))

def rcv(target):
    if get(target) != 0:
        print(sounds[-1])
        sys.exit(0)

def jgz(target, offset):
    if get(target) > 0:
        return get(offset)

def run():
    global ip
    instruction = instructions[ip]
    offset = 1

    offset = globals()[instruction['op']](*instruction['params'])

    ip += 1 if offset is None else offset

def execute():
    while ip < len(instructions):
        run()

print(execute())
