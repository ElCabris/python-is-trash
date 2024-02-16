# Crear un programa que genere una matriz de números y la imprima en pantalla.

import random

filas = int(input("ingrese la cantidad de filas: "))
columnas = int(input("ingrese la cantidad de columnas: "))

inferior, superior = input("ingrese el rango inferior y superior (ambos inclusivos): ").split()

inferior = int(inferior)
superior = int(superior)

solution = []

for i in range(filas):
    solution.append([])
    for j in range(columnas):
        solution[i].append(random.randint(inferior, superior))

for i in solution:
    print(i)
    