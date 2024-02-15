# Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.

import random

cantidad = int(input("ingrese la cantidad de elementos de la lista: "))
inferior = int(input("ingrese el líminte inferior (inclusivo): "))
superior = int(input("ingrese el límite superior (inclusivo): "))

aleatorios = []
for i in range(cantidad):
    aleatorios.append(random.randint(inferior, superior))

print(aleatorios)
