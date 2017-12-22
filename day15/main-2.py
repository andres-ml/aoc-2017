import sys
import re

A = 873
B = 583

factorA = 16807
factorB = 48271

divisor = 2147483647

count = 0
loops = int(5e6)

length = 16
bits = lambda n : bin(n)[2:].zfill(length)[-length:]

def gen(x, factor, mod):
    while True:
        x = (x * factor) % divisor
        if x % mod == 0:
            yield x

a, b = gen(A, factorA, 4), gen(B, factorB, 8)
for _ in range(loops):
    if bits(next(a)) == bits(next(b)):
        count += 1
        
print(count)
