from collections import deque

#Creamos el objeto Pila
pila = deque()

#Verificar si la pila esta vacia
print(len(pila) == 0)

#Agregando elementos a la pila
pila.append(1)
pila.append(2)
pila.append(3)
pila.append(4)
pila.append(5)

#Verificar si la pila esta vacia
print(len(pila) == 0)

#Mostrar la Pila
print(pila)

#Sacar el primer elemento de la pila
pila.pop()

#Mostrar la Pila
print(pila)

#Sacar el primer elemento de la pila
pila.pop()
pila.pop()
pila.pop()
pila.pop()

#Verificar si la pila esta vacia
print(len(pila) == 0)


