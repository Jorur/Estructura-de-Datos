class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.sgte = None

class ListaEnlazadaCircular:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, valor):
        nodo = Nodo(valor)

        if self.cabeza:
            self.cabeza.sgte = nodo
            self.cabeza = nodo
            self.cabeza.sgte = self.cola

        else:
            self.cabeza = nodo
            self.cola = nodo

    def recorrer(self):
        actual = self.cola

        while actual:
            valor = actual.valor
            actual = actual.sgte
            yield valor

#Principal

LC = ListaEnlazadaCircular()
LC.agregar(1)
LC.agregar(2)
LC.agregar(3)
LC.agregar(4)

for val in LC.recorrer():
    print(val)
