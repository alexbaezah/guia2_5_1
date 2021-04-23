numeros = []

for i in range(3):
    i = int(input(f"introduce el numero {i + 1} "))
    numeros.append(i)
print(numeros)

for pos in numeros: 
    if pos > 0:
        print(f"{pos} es positivo")
    else:
        print(f"{pos} es negativo")
        