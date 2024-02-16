# Escribir una función que calcule el área de un círculo dado su radio.

import math

def radio(rad):
    return math.pi * (rad ** 2)

r = float(input())

print(radio(r))
