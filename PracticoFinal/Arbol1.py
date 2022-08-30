'''Supongamos que tenemos una función valor tal que dado un valor de 
tipo char (una letra del alfabeto) devuelve un valor entero asociado a dicho 
identificador. Supongamos también la existencia de un árbol de 
expresión T cuyos nodos hoja son letras del alfabeto y cuyos nodos 
interiores son los caracteres *, +, -, /. Diseñar un programa en Python que
tome como parámetros un nodo y un árbol binario y devuelva el resultado 
entero de la evaluación de la expresión representada.'''

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def InsertarA(raiz, nodo):
    if raiz is None:
        raiz = nodo

    else:
        if raiz.valor > nodo.valor:
            if raiz.izq is None:
                raiz.izq = nodo

            else:
                InsertarA(raiz.izq, nodo)

        else:
            if raiz.der is None:
                raiz.der = nodo

            else:
                InsertarA(raiz.der, nodo)

def hoja(nodo):
    return nodo.izq is None and nodo.der is None 

def proceso(op, x, y):
    if op == "+":
        return x+y

    elif op == "-":
        return x-y
    
    elif op == "*":
        return x*y

    elif op == "/":
        return x/y

def evaluar(raiz):
    if raiz is None:
        return 0

    if hoja(raiz):
        return ord(raiz.valor)

    x = evaluar(raiz.izq)
    y = evaluar(raiz.der)

    return proceso(raiz.valor, x, y)
    
    
#Principal
raiz = Nodo("+") 
raiz.izq = Nodo("*")
raiz.der = Nodo("/")
raiz.izq.izq = Nodo("-")
raiz.izq.der = Nodo("A")
raiz.der.izq = Nodo("D")
raiz.der.der = Nodo("N")
raiz.izq.izq.izq = Nodo("Z")
raiz.izq.izq.der = Nodo("P")

print(f"El valor total de la expresion es: {evaluar(raiz)}")

