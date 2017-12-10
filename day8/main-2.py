import sys
import re
from pprint import pprint

def match(regex, string, keys):
    matches = re.search(regex, string)
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = matches.group(i + 1)

    return result

def read(instruction):
    return match(r"([a-z]+) (inc|dec) (-?\d+) if ([a-z]+) (==|<=|>=|<|>|!=) (-?\d+)", instruction, ['target', 'op', 'by', 'conditioner', 'comparator', 'value'])


instructions = []
state = {}

for line in sys.stdin.read().splitlines():
    instruction = read(line)
    instruction['by'] = int(instruction['by'])
    instruction['value'] = int(instruction['value'])
    instructions.append(instruction)

    state[instruction['target']] = 0
    state[instruction['conditioner']] = 0

def run(instruction):
    must_run = False
    if instruction['comparator'] == '==':
        must_run = state[instruction['conditioner']] == instruction['value']
    elif instruction['comparator'] == '<=':
        must_run = state[instruction['conditioner']] <= instruction['value']
    elif instruction['comparator'] == '>=':
        must_run = state[instruction['conditioner']] >= instruction['value']
    elif instruction['comparator'] == '<':
        must_run = state[instruction['conditioner']] < instruction['value']
    elif instruction['comparator'] == '>':
        must_run = state[instruction['conditioner']] > instruction['value']
    elif instruction['comparator'] == '!=':
        must_run = state[instruction['conditioner']] != instruction['value']

    if must_run:
        state[instruction['target']] += instruction['by'] * (1 if instruction['op'] == 'inc' else -1)
        
    return max(state.values())

print(max(run(instruction) for instruction in instructions))