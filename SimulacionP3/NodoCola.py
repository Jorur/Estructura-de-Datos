# Cola, Jorge Urioste
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

class Cola:
    def __init__ (self):
        self.elementos = []

    def mete (self, nodo):
        self.elementos.append(nodo)

    def saca (self):
        if len(self.elementos) != 0:
            return self.elementos.pop(0)
    
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

#Crear una cola 
Q = Cola()

n = primero
while n is not None:
    print(n.datos)
    Q.mete(n.datos.nombre)
    n = n.siguiente

print("La cola original es: ")
Q.lista()

print("Eliminamos al alumno: ", Q.saca())

print("La cola nueva es: ")
Q.lista()

