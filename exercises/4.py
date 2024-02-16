# Escribir un programa que determine si un número dado es par o impar.

n = int(input("ingrese un número: "))

print(f"{n} es", end=" ")

if n % 2 == 0:
    print("par")
else:
    print("impar")