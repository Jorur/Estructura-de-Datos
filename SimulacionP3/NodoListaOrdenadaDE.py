#Lista doblemente enlazada, Jorge Urioste Hurtado
class Alumno:
    def __init__ (self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def __str__ (self):
        return self.nombre + ' - '+ str(self.edad)+ ' años: '+ str(self.nota)

class Nodo:
    def __init__ (self, datos):
        self.datos = datos
        self.siguiente = None

class Node:
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
        nodo = Node(valor)

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
        nodo = Node(valor)

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

    def eliminar(self, x):
        actual = self.cabeza
        anterior = self.cabeza

        while actual:
            if actual.valor == x:
                if actual == self.cola:
                    self.cola = actual.sgt

                else:
                    anterior.sgt = actual.sgt

                return
            anterior = actual
            actual = actual.sgt

#Principal
primero = None
alumno = Alumno("Alex", 30, 8.9)
nodo = Nodo(alumno)
nodo.siguiente = primero
primero = nodo


alumno = Alumno("Pepe", 27, 3.7)
nodo = Nodo(alumno)
nodo.siguiente = primero
primero = nodo

alumno = Alumno("Jorge", 20, 9.2)
nodo = Nodo(alumno)
nodo.siguiente = primero
primero = nodo

#Crear una LD
ld = ListaDoble()

n = primero
while n!= None:
    print(n.datos)
    ld.agregar(n.datos.nombre)
    n = n.siguiente

for val in ld.recorrer():
    print(val)

ld.eliminar("Pepe")

print("Nueva Lista: ")
for val in ld.recorrer():
    print(val)


