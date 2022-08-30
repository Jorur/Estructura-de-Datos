class Cola:
    #Inicia la cola 
    def __init__ (self):
        self.elementos = []

    #Metodo para insertar valores a la cola
    def Insertar(self, valor):
        self.elementos.append(valor)
        return valor

    #Metodo para saber si la cola esta vacia
    def Vacia(self):
        return len(self.elementos) == 0

    #Metodo para eliminar el valor de una cola
    def Eliminar(self):
        return self.elementos.pop(0) # .pop elimina el elemento que se le asigna o por defecto el ultimo

    #Metodo para ver el primer elemento de la cola
    def Primero(self):
        return self.elementos[0]

    #Metodo Para ver el ultimo elemento de una cola
    def Ultimo(self):
        return self.elementos[-1]

#Implementar la clase Cola
if __name__ == '__main__':
    cola = Cola()

    #Verificar que la cola este vacia
    print(cola.Vacia())
    cola.Insertar(1)
    cola.Insertar(2)
    cola.Insertar(3)
    cola.Insertar(4) 
    cola.Insertar(5)

    #Verificar que la cola este vacia
    print(cola.Vacia())
    
    #Mostrar elementos de la cola
    print(cola.elementos)

    #Mostrar primer y ultimo elemento
    print("El primer elemento de la cola es:", cola.Primero())
    print("El ultimo elemento de la cola es:", cola.Ultimo())

    #Quitar elementos de la cola
    cola.Eliminar()
    cola.Eliminar()
    cola.Eliminar()
    cola.Eliminar()
    cola.Eliminar()

    #Verificar que la cola este vacia
    print(cola.Vacia())