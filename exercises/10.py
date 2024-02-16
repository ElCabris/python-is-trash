# Escribir una función que calcule el factorial de un número dado.

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("ingresa el número: "))

print(factorial(number))
