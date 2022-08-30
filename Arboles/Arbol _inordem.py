#Crear una Clase para la busqueda Binaria 
class Nodo:
    def __init__(self, nodo):
        self.izq = None
        self.der = None 
        self.valor = nodo 

def insertarArbol(raiz, nodo):
    if raiz is None:
        raiz = nodo 
        
    else: 
        if raiz.valor > nodo.valor:
            if raiz.izq is None:
                raiz.izq = nodo
            
            else:
                insertarArbol(raiz.izq, nodo)
        else:
            if raiz.der is None:
                raiz.der = nodo
            else:
                insertarArbol(raiz.der, nodo)

def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izq)
        print(raiz.valor)
        inorden(raiz.der)
    


raiz = Nodo(14) 
insertarArbol(raiz, Nodo(2))
insertarArbol(raiz, Nodo(15))
insertarArbol(raiz, Nodo(4))
insertarArbol(raiz, Nodo(16))
insertarArbol(raiz, Nodo(5))
insertarArbol(raiz, Nodo(18))

inorden(raiz)