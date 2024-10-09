#Find The greatest common divisor of multiple numbers read from the console.

import math
from functools import reduce

numere = input("Introdu numerele : ")

lista_numere = list(map(int, numere.split()))

cmmdc = reduce(math.gcd, lista_numere)

print("CMMDC:", cmmdc)
