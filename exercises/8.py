# Crear una función que invierta el orden de los elementos en una lista dada.

def invert(lista):
    return lista[::-1]


listica = input("ingrese la lista separando por espacio sus elementos: ").split()

print(invert(listica))