from collections import deque


from collections import deque

#Crear un objeto Cola
cola = deque()

#Verificar si la cola esta vacia
print(len(cola) == 0)
cola.append(1)
cola.append(2)
cola.append(3)
cola.append(4)
cola.append(5)

#Verificar si la cola esta vacia
print(len(cola) == 0)

#Mostrar elementos de la cola 
print(cola)

#Quitar elementos 
cola.popleft()
cola.popleft()
cola.popleft()
cola.popleft()
cola.popleft()

#Verificar si la cola esta vacia 
print(len(cola) == 0)