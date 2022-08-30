#Crear una funcion Lambda para contar la cantidad de numeros pares impares 

lista = list(range(1, 14))

print(lista)
print()

Pares = list(filter(lambda n: n%2 == 0, lista))
print(Pares)

Impares = list(filter(lambda n: n%2 != 0, lista))
print(Impares)