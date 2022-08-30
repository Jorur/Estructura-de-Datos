#Arbol Impreso en Pre Orden

class Nodo:
    def __init__ (self, nodo):
        self.izq = None
        self.der = None
        self.valor = nodo

def Insertar(raiz, nodo):
    if raiz is None:
        raiz = nodo

    else:
        if raiz.valor > nodo.valor:
            if raiz.izq is None:
                raiz.izq = nodo 

            else:
                Insertar(raiz.izq, nodo)

        else:
            if raiz.der is None:
                raiz.der = nodo

            else:
                Insertar(raiz.der, nodo)

def Preorden(raiz):
    if raiz is not None:
        print(raiz.valor)
        Preorden(raiz.izq)
        Preorden(raiz.der)





raiz = Nodo(14) 
Insertar(raiz, Nodo(2))
Insertar(raiz, Nodo(15))
Insertar(raiz, Nodo(4))
Insertar(raiz, Nodo(16))
Insertar(raiz, Nodo(5))
Insertar(raiz, Nodo(18))

Preorden(raiz)