import sys

input = sys.stdin.read()
offset = int(input)

loops       = int(50e6)
position    = 0
val         = None

for i in range(1, loops + 1):
    position = (position + offset) % i + 1
    # 0 is always at the start; the value after 0 is at position=1
    if position == 1:
        val = i

print(val)