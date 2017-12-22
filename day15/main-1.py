import sys
import re

A = 873
B = 583

factorA = 16807
factorB = 48271

divisor = 2147483647

count = 0
loops = int(40e6)

length = 16
bits = lambda n : bin(n)[2:].zfill(length)[-length:]

for _ in range(loops):
    A = (A * factorA) % divisor
    B = (B * factorB) % divisor
    
    if bits(A) == bits(B):
        count += 1
        
print(count)
