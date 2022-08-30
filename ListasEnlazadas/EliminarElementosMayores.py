#Crear la clase nodo

class Nodo():
    def __init__ (self, valor):
        self.valor = valor
        self.sgte = None

class ListaEnlazada:
    def __init__ (self):
        self.cabeza = None
        self.cola = None
        self.size = 0

    def agregar(self, valor):
        nodo = Nodo(valor)

        if self.cabeza:
            self.cabeza.sgte = nodo
            self.cabeza = nodo
            self.size += 1

        else:
            self.cabeza = nodo
            self.cola = nodo
            self.size += 1

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
            if actual.valor > x:
                if actual == self.cola:
                    self.cola = actual.sgte
                    self.size -= 1

                else:
                    anterior.sgte = actual.sgte
                    self.size -= 1
                    
                    return
            anterior = actual
            actual = actual.sgte

    def buscar(self, valor):
        for val in self.recorrer():
            if val == valor:
                return True
            
            else:
                return False
        
Valores = ListaEnlazada()

Valores.agregar(78)
Valores.agregar(33)
Valores.agregar(45)
Valores.agregar(81)
Valores.agregar(26)



for val in Valores.recorrer():
    print(val)


print()
print("Lista normal: ")
for val in Valores.recorrer():
    print(val)

x = 35

for i in range (Valores.size):
    Valores.eliminar(33)

print()
print("Lista Nueva: ")
for val in Valores.recorrer():
    print(val)




