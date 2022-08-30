from queue import PriorityQueue

estudiantes = PriorityQueue()

estudiantes.put((1, "A"))
estudiantes.put((4, "B"))
estudiantes.put((3, "C"))
estudiantes.put((2, "D"))
estudiantes.put((5, "E"))

while estudiantes:
    print(estudiantes.get())


