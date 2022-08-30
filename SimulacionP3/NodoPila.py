# Pila, Jorge Urioste
class Alumno:
    def __init__ (self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def __str__ (self):
        return self.nombre + '-'+ str(self.edad)+ ' años: '+ str(self.nota)

class Nodo:
    def __init__ (self, datos):
        self.datos = datos
        self.siguiente = None

class Pila:
    def __init__(self):
        self.elementos = []

    def mete(self, nodo):
        self.elementos.append(nodo)

    def saca(self):
        if len(self.elementos) != 0:
            return self.elementos.pop()

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

#Crear una Pila
p = Pila()


n = primero
while n!= None:
    print(n.datos)
    p.mete(n.datos.nombre)
    n = n.siguiente

print("La pila original es: ")
p.lista()

print("El elemento que sale es:",p.saca())

print("La pila con elemento borrado es: ")
p.lista()
    