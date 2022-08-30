class Nodo:
    def __init__ (self, valor):
        self.valor = valor
        self.sgte = None

    def __str__(self):
        return str(self.valor)

class ListaEnlazada:
    def __init__ (self):
        self.primero = None
        self.size = 0

    def agregar(self, valor):
        nodo = Nodo(valor)
        if self.size == 0:
            self.primero = nodo

        else:
            actual = self.primero
            while actual.sgte is not None:
                actual = actual.sgte
            actual.sgte = nodo
        self.size = self.size + 1
        
    def __str__ (self):
        actual = self.primero
        String =''
        while actual is not None:
            String +=str(actual)
            String += ''
            actual = actual.sgte
        return String

    def eliminar(self, x):
        if self.size == 0:
            return False

        else:
            try:
                actual = self.primero
                while actual.sgte.valor != x:
                    actual = actual.sgte

                borrar = actual.sgte
                actual.sgte = borrar.sgte

            except AttributeError:
                print(f'El valor: {x} no existe!!!')
                return False

        self.size -= 1

    def buscar (self, valor):
        actual = self.primero 

        while actual:
            if actual.valor == valor:
                return True 

            else:
                actual = actual.sgte

        return False


#Implementar
miLista = ListaEnlazada()
miLista.agregar(5)
miLista.agregar(2)
miLista.agregar('A')
miLista.agregar('[]')
miLista.agregar('B')
print(miLista)
print(miLista.buscar(8))
