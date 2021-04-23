suma = 0
while suma < 10:
     numero_1 = int(input("ingrese el primer número "))
     numero_2 = int(input("ingrese el segundo número "))
     numero_3 = int(input("ingrese el tercer número "))
     suma = numero_1 + numero_2 + numero_3
     if suma > 10:
         print(f"la suma de {suma} es mayor que 10")
     elif suma < 10:
          print(f"la suma de {suma} es menor que 10, ingresa nuevamente los 3 números")
    
