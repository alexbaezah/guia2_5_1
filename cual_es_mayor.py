numero_1 = int(input("ingrese un número entero positivo "))
numero_2 = int(input("ingrese un segundo número entero positivo "))
if (numero_1 and numero_2 > 0) and (numero_1 > numero_2):
    print(f"numero {numero_1} es mayor que {numero_2}")
elif (numero_1 and numero_2 > 0) and (numero_2 > numero_1):
    print(f"numero {numero_2} es mayor que {numero_1}")
elif (numero_1 and numero_2 < 0):
    print(f"ambos números, {numero_1} y {numero_2} son menores que cero")
