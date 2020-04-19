# Write code that calculates Pi using Archimedes method to 100 places.

from decimal import *

getcontext().prec = 101

pi = 0
n = 6
s = 1

for i in range(165):
    a = Decimal(((1 ** 2) - (s / 2) ** 2)).sqrt()
    b = Decimal(1) - Decimal(a)
    pi = Decimal(n * s) / Decimal(2)
    halfS = Decimal(s) / Decimal(2)
    s = Decimal((b ** 2) + (halfS ** 2)).sqrt()
    n = n * 2
res = format(pi, '.99f')
print(res)
