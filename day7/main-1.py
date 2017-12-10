import sys
import re

programs = {}
regex = r"(\w+) \((\d+)\)(?: -> (.+))?"

for line in sys.stdin.read().splitlines():
    match = re.search(regex, line)

    name        = match.group(1)
    weight      = int(match.group(2))
    childList   = match.group(3)

    children = [] if childList == None else childList.split(', ')

    programs[name] = {
        'weight': weight,
        'children': children,
    }

def find_base():
    all = programs.keys()
    children = [child for sublist in programs.values() for child in sublist['children']]
    return next(x for x in all if x not in children)

print(find_base())
