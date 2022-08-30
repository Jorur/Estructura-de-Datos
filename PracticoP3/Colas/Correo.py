class Persona:
    def __init__ (self, nombre, num):
        self.cartas = num
        self.nombre = nombre

    def __str__ (self):
        return f"{self.nombre}, {self.cartas}"

class Correo:
    def __init__(self, cantidad):
        self.cola = []
        self.limite = cantidad

    def agregar(self, nombre, num):
        persona = Persona(nombre, num)
        self.cola.append(persona)
   
    def eliminar(self):
       return self.cola.pop(0)
    
    def mover(self):
        if self.cola[0].cartas <= self.limite:
            self.eliminar()

        else: 
            aux = self.eliminar()
            self.agregar(aux.nombre, (aux.cartas-self.limite))

#Principal
cola = Correo(5)
cola.agregar("Jorge", 4)
cola.agregar("Oscar", 7)
cola.agregar("Nicole", 3)
cola.agregar("Mateo", 3)

print("Cola Inicial: ")
for nombre in cola.cola:
    print(nombre)  

print()
cola.mover()

print("Cola siguiente: ")
for nombre in cola.cola:
    print(nombre)  


print()
cola.mover()

print("Cola final: ")
for nombre in cola.cola:
    print(nombre)  




    
