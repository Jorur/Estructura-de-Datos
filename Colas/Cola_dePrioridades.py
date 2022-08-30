from queue import PriorityQueue

#Creamos la clase para probar las colas de prioridad
class Curso:
    def __init__ (self, prioridad, nombre):
        self.prioridad = prioridad
        self.nombre = nombre 

    def __lt__ (self, other):
       return self.prioridad  < other.prioridad

def agregar(curso, prioridad, nombre):
    curso.put(Curso(prioridad, nombre))

def extraer(curso):
    curso.get()
#Implementar Prioridades
cursos = PriorityQueue()

#Agregar elementos a la cola de Prioridades
cursos.put(Curso(4, "Jassiel"))
cursos.put(Curso(3, "Mateo"))
cursos.put(Curso(1, "Emiliana"))
cursos.put(Curso(5, "Jorge"))
cursos.put(Curso(2, "Ana"))
agregar(cursos,6, "Rolando")
extraer(cursos)

#Mostrar los elementos de la cola con sus prioridades 
while not cursos.empty():
    c = cursos.get()
    print(c.prioridad, c.nombre)