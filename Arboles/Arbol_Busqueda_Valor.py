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


def Busqueda(raiz, x):
    if raiz is None:
        return False

    else:
        if raiz.valor == x:
            return True

        else:
            if raiz.valor > x:

                if raiz.izq == x:
                    return True

                else:
                    return Busqueda(raiz.izq, x)

            else:
                if raiz.der == x:
                    return True

                else:
                    return Busqueda(raiz.der, x)

raiz = Nodo(14) 
Insertar(raiz, Nodo(2))
Insertar(raiz, Nodo(15))
Insertar(raiz, Nodo(4))
Insertar(raiz, Nodo(16))
Insertar(raiz, Nodo(5))
Insertar(raiz, Nodo(18))

x = int(input("Valor: "))
print(Busqueda(raiz, x))
            
        
