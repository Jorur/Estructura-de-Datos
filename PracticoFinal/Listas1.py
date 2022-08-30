class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.sgte = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, valor):
        nodo = Nodo(valor)

        if self.cabeza:
            self.cabeza.sgte = nodo
            self.cabeza = nodo

        else:
            self.cabeza = nodo
            self.cola = nodo

    def recorrer(self):
        actual = self.cola

        while actual:
            valor = actual.valor
            actual = actual.sgte
            yield valor

    def eliminar(self, x):
        actual = self.cola
        anterior = self.cola

        while actual:
            if actual.valor == x:
                if actual == self.cola:
                    self.cola = actual.sgte

                else:
                    anterior.sgte = actual.sgte
                return

            anterior = actual
            actual = actual.sgte

#Principal
L1 = ListaEnlazada()
L2 = ListaEnlazada()

L1.agregar(4)
L1.agregar(6)
L1.agregar(7.5)
L1.agregar(8)


L2.agregar(4)
L2.agregar(9)
L2.agregar(12)
L2.agregar(5.25)
L2.agregar(13)
L2.agregar(7)

media= 0
cont = 0
for val in L1.recorrer():
    if type(val) != float:
        print(val)
    media += val
    cont += 1

media /= cont

print(f"La media es: {media}")
print("Los valores mayores a la media de la segunda lista son: ")

for valores in L2.recorrer():
    if valores > media:
        print(valores)