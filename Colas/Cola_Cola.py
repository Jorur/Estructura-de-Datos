from queue import Queue

#Crear el onjeto Cola
cola_obj = Queue()

#Verificar si la cola esta vacia 
print(cola_obj.empty())

#Ingresar elementos a la cola
cola_obj.put(1)
cola_obj.put(2)
cola_obj.put(3)
cola_obj.put(4)
cola_obj.put(5)

#Verificar si la cola esta vacia 
print(cola_obj.empty())

#Mostrar los elementos de la cola 
print(cola_obj.queue)

#Mostrar el tamano de la cola 
print("El tamano de la cola es:", cola_obj.qsize())

#Quitar elementos de una cola
cola_obj.get()
cola_obj.get()
cola_obj.get()
cola_obj.get()
cola_obj.get()

#Verificar si la cola esta vacia 
print(cola_obj.empty())