#Crear la clase nodo

class Nodo:
    def __init__ (self, valor):
        self.valor = valor
        self.sgte = None

class ListaEnlazada:
    def __init__ (self):
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
        aux = list()
        while actual:
            valor = actual.valor
            actual = actual.sgte
            aux.append(valor)

        return aux
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

    def buscar(self, valor):
        for val in self.recorrer():
            if val == valor:
                return True
            
            else:
                return False

    

    def __str__(self):
        return f"La lista enlazada es: {self.recorrer()}"
            
Valores = ListaEnlazada()

Valores.agregar(3)
Valores.agregar(5)
Valores.agregar(7)
Valores.agregar(9)



Valores.eliminar(5)
print()


print(Valores.buscar(3))

print(Valores)
