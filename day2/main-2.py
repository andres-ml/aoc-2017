import fileinput
import re

numbers = []

for line in fileinput.input():
    numbers.append([int(n) for n in re.split(r'[ \t]+', line)])

def divisible(items) :
    indices = range(len(items))
    for i in indices :
        for j in indices :
            if (i != j and items[i] % items[j] == 0):
                return items[i] // items[j]

checksum = sum([divisible(row) for row in numbers])

print(checksum)
