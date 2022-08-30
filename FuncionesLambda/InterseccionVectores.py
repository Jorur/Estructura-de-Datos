#Interseccion de 2 vectores utilizando funcion lambda
V1 =[2, 3, 5, 11, 13]
V2 = [1, 4, 5, 3, 11, 10, 19, 23]

print(V1)
print(V2)

print()

resultado = list(filter(lambda n: n in V1, V2))
print(resultado)