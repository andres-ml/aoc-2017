import fileinput
import re

numbers = []

for line in fileinput.input():
    numbers.append([int(n) for n in re.split(r'[ \t]+', line)])

checksum = sum([max(row) - min(row) for row in numbers])

print(checksum)
