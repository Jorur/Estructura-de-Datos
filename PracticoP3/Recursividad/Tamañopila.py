class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        self.elementos.pop()



def Tamano(pila, i):
    if i == len(pila.elementos):
        return 0

    else:
        return 1 +Tamano(pila, i+1)

#Principal
p =Pila()
p.apilar(1)
p.apilar(2)
p.apilar(3)
p.apilar(4)
print("El tamano de la pila es de:",Tamano(p, 0))