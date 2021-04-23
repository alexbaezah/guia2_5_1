numeros = []
for i in range(3):
  """se pone {i + 1} porque i es el ciclo, entonces 
      parte de 0 el primero ahí imprime introduce el 
      numero 1, 2 o 3 según el caso"""
  numero = float(input(f"Introduce el número {i + 1}: "))
  numeros.append(numero)
print(numeros)

menor = numeros[0]
#numeros[0] acá puede ir cualquier numero de la matriz, ya que abajo compara y sale el menor
#aca se itera con for
# para numero (variable donde alberga el ciclo)
# entonces cada ciclo impreso en print(numero) corresponde a numeros[0], numeros[1] y numeros[2]
for numero in numeros:
    print(numero)
    if numero < menor:
        menor = numero
 

print(f"el numero menor de {numeros} es {menor}")

        
