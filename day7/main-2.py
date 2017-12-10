import sys
import re
import statistics

programs = {}

# parse input
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

# find root; aka program that is not a child of any other
def find_base():
    all = programs.keys()
    children = [child for sublist in programs.values() for child in sublist['children']]
    return next(x for x in all if x not in children)

base = find_base()

# fill weights: add info about children weight to each program
def fill_weights(root=base):
    programs[root]['holding'] = sum(fill_weights(child) for child in programs[root]['children'])
    programs[root]['total'] = programs[root]['weight'] + programs[root]['holding']
    return programs[root]['total']

fill_weights()

# find unbalanced program
def find_unbalanced(root, expected=None):
    children = root['children']
    # find expected weight
    mode = statistics.mode(map(lambda name: programs[name]['total'], children))
    # find node that does not match expected weight
    unbalanced_child = next((programs[name] for name in children if programs[name]['total'] != mode), None)
    # search in that node if it exists
    if unbalanced_child != None :
        # pass expected weight so we can later calculate the needed weight
        return find_unbalanced(unbalanced_child, mode)
    # otherwise the problem is the current program's weight; the needed weight is the expected one minus the childrens' weights
    return expected - mode*len(children)

print(find_unbalanced(programs[base]))
