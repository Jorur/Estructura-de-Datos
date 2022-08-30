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

def Buscar(raiz, x):
    if raiz is None:
        return False

    elif raiz.valor == x:
        return True

    elif raiz.valor > x:
        return Buscar(raiz.izq, x)

    else:
        return Buscar(raiz.der, x)

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.valor)
        inorden(raiz.der)


raiz = Nodo(14) 
Insertar(raiz, Nodo(2))
Insertar(raiz, Nodo(15))
Insertar(raiz, Nodo(4))
Insertar(raiz, Nodo(16))
Insertar(raiz, Nodo(5))
Insertar(raiz, Nodo(18))

inorden(raiz)

x = int(input("Valor: "))

print(Buscar(raiz, x))
          