from queue import LifoQueue

#Creamos el objeto Pila

pila = LifoQueue()

#Verificar si la pila esta vacia
print(pila.empty())

#Agregando elementos a la pila 
pila.put(1)
pila.put(2)
pila.put(3)
pila.put(4)
pila.put(5)

#Verificar si la pila esta vacia
print(pila.empty())

#Mostrar la pila
print(pila.queue)

#Sacar elementos de la pila
pila.get()
pila.get()
pila.get()
pila.get()
pila.get()

#Verificar si la pila esta vacia
print(pila.empty())