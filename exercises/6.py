# Crear un programa que calcule la suma de los números en una lista dada.

lista = input("ingrese los elmentos de la lista separados por un espacio: ").split()
lista = [float(i) for i in lista]

solution = 0

for i in lista:
    solution += i

print(solution)
