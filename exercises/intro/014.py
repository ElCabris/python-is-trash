# Escribir una función que calcule la media aritmética de una lista de números.

def promedio(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma / len(lista)

numeros = input().split()

numeros = [float(i) for i in numeros]

print(promedio(numeros))