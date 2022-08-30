class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None


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

def hoja(nodo):
    if nodo:
        return nodo.izq is None and nodo.der is None 


def eliminarH(raiz):
    if raiz is None:
        return False

    if hoja(raiz.izq):
        raiz.izq = None

    if hoja(raiz.der):
        raiz.der = None

    eliminarH(raiz.izq)
    eliminarH(raiz.der)

  

#Principal
raiz = Nodo("K")
Insertar(raiz, Nodo("G"))
Insertar(raiz, Nodo("C"))
Insertar(raiz, Nodo("B"))
Insertar(raiz, Nodo("D"))
Insertar(raiz, Nodo("H"))
Insertar(raiz, Nodo("Q"))
Insertar(raiz, Nodo("M"))
Insertar(raiz, Nodo("Y"))
Insertar(raiz, Nodo("P"))

eliminarH(raiz)
Preorden(raiz)
print()
eliminarH(raiz)
Preorden(raiz)

print()
eliminarH(raiz)
Preorden(raiz)
