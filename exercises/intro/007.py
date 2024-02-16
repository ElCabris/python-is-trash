# Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada

n = input().split()

n = [float(i) for i in n]

print(f"minimo {min(n)} \nmaximo {max(n)}")
