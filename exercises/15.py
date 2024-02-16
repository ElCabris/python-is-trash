# Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.

n = input("ingrese una palabra: ")
print(n, end=" ")
if n == n[::-1]:
    print("es palindromo")
else:
    print("no es palindromo")