from random import randrange

class Avion:
    def __init__(self, prioridad, numero):
        self.prioridad = prioridad
        self.numero = numero
        

class TorredeControl:
    def __init__(self):
        self.aterrizar = []
        self.despegar = []
    
    def reconocimiento(self, prioridad, numero):
        avion = Avion(prioridad, numero)
        if avion.prioridad == 1:
            self.aterrizar.append(avion)

        else:
            self.despegar.append(avion)

    def accion(self):
        if len(self.aterrizar) != 0:
            print(f"El avion {self.aterrizar[0].numero} ha aterrizado")
            self.aterrizar.pop(0)

        else:
            print(f"El avion {self.despegar[0].numero} ha despegado")
            self.despegar.pop(0)

    def __str__(self):
        return f"El estado de la cola de aterrizajes es {len(self.aterrizar) != 0}, y de la cola de despegue {len(self.despegar) != 0}"

#Principal
Q = TorredeControl()
Q.reconocimiento(randrange(2),"avion 1")
print(Q)
print()

Q.reconocimiento(randrange(2),"avion 2")
print(Q)
print()

Q.reconocimiento(randrange(2),"avion 3")
print(Q)
print()

Q.accion()
print(Q)
print()

Q.accion()
print(Q)
print()

Q.accion()
print(Q)



        




