class Nodo:
    def __init__ (self, valor):
        self.valor = valor
        self.ant = None
        self.sgt = None

class ListaDoble:

    def __init__ (self):
        self.cabeza = None
        self.cola = None
        self.size = 0

    def agregar(self, valor):
        nodo = Nodo(valor)

        if self.cola is None:
            self.cabeza = nodo
            self.cola = self.cabeza
            self.size += 1

        else:
            nodo.ant = self.cola
            self.cola.sgt = nodo
            self.cola = nodo
            self.size += 1

    def primero(self, valor):
        nodo = Nodo(valor)

        if self.cabeza:
            nodo.sgt = self.cabeza
            self.cabeza.ant = nodo
            self.cabeza = nodo

        else:
            self.agregar(valor)
        

    def recorrer(self):
        actual = self.cabeza

        while actual:
            valor = actual.valor
            actual = actual.sgt
            yield valor

    def invertir(self):
        anterior = None
        self.cola, self.cabeza = self.cabeza, self.cola
        print("El valor de la cola es: ",self.cabeza.valor)
        while self.cola:
            siguiente = self.cola.sgt
            self.cola.sgt= anterior
            self.cola.ant = siguiente
            anterior = self.cola
            self.cola= siguiente

    




#Principal
Lista = ListaDoble()
Lista.agregar(7)
Lista.agregar(4)

print("Lista 1:")
for val in Lista.recorrer():
    print(val)


print("Lista 2:")
Lista.primero(5)
Lista.agregar(3)

for val in Lista.recorrer():
    print(val)

print("Lista invertida")
Lista.invertir()
for val in Lista.recorrer():
    print(val)


