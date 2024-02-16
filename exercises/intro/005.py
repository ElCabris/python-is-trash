# Crear una función que convierta grados Fahrenheit a grados Celsius.

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)


grados_f = float(input("ingresa los grados fahrenheit: "))

print(fahrenheit_to_celsius(grados_f))