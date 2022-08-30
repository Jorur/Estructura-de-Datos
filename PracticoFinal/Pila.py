class Pila:
    def __init__(self):
        self.elementos = []

    def ingresar(self,valor):
        return self.elementos.append(valor)

    def eliminar(self):
        return self.elementos.pop()


def Meter(pila, palabra):
    for i in range (len(palabra)//2):
        pila.ingresar(palabra[i])

def evaluar(pila, palabra):
    if len(palabra)%2 == 0:
        for i in range(len(palabra)//2, len(palabra)):
            if palabra[i] != pila.eliminar():
                return False
        return True

    else:
        for i in range(len(palabra)//2+1, len(palabra)):
            if palabra[i] != pila.eliminar():
                return False
        return True

#Principal
p = Pila()
palabra = "erre"
Meter(p, palabra)
print(evaluar(p, palabra))
