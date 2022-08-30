# Lista Ordenda, Jorge Urioste
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

class ListaOrdenada:
    def __init__(self):
        self.elementos = []

    def mete(self, nodo):
        self.elementos.append(nodo)
        self.elementos.sort()

    def saca(self, nombre):
        if len(self.elementos) != 0:
            for i in range(len(self.elementos)):
                if self.elementos[i] == nombre:
                    return self.elementos.pop(i)

    def lista(self):
        if len(self.elementos) != 0:
            print(self.elementos) 

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

#Crear Lista ordenada
l = ListaOrdenada()

n = primero
while n is not None:
    print(n.datos)
    l.mete(n.datos.nombre)
    n = n.siguiente

print("Lista ordenada: ")
l.lista()

print("La nueva lista ordenada es: ")
l.saca("Jorge")
l.lista()


