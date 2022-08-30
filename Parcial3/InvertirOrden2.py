#Pregunta 2, Jorge Urioste Hurtado
class Cola:
    #Inicia la cola 
    def __init__ (self):
        self.elementos = []

    #Metodo para insertar valores a la cola
    def agregar(self, valor):
        self.elementos.append(valor)

    #Metodo para saber si la cola esta vacia
    def Vacia(self):
        return len(self.elementos) == 0

    #Metodo para eliminar el valor de una cola
    def Eliminar(self):
        return self.elementos.pop(0) # .pop elimina el elemento que se le asigna o por defecto el ultimo

    #Metodo para ver el primer elemento de la cola
    def Primero(self):
        return self.elementos[0]

    #Metodo Para ver el ultimo elemento de una cola
    def Ultimo(self):
        return self.elementos[-1]

    def cantidad(self):
        cont = 0
        for i in range(len(self.elementos)):
            cont += 1

        return cont 

    def invertir(self):
        aux= []
        for i in range(len(self.elementos)):
            aux.append(self.elementos.pop())
        
        for i in range(len(aux)):
            self.agregar(aux[i])
        
        return self.elementos

        
        

class Pila:
    def __init__ (self):
        self.elementos = []
    
    def apilar(self, valor ):
        self.elementos.append(valor)

    def Desapilar(self):
        self.elementos.pop()

    def Vacio(self):
        return len(self.elementos) == 0

    def top(self):
        return self.elementos[-1]

    def cantidad(self):
        cont = 0
        for i in range(len(self.elementos)):
            cont += 1
        return cont
    
    def invertir(self):
        aux= []
        for i in range(len(self.elementos)):
            aux.append(self.elementos.pop())
        
        for i in range(len(aux)):
            self.apilar(aux[i])
        
        return self.elementos

class Nodo:
    def __init__ (self, valor):
        self.valor = valor
        self.sgte = None

class ListaEnlazada:
    def __init__ (self):
        self.cabeza = None
        self.cola = None

    def agregar(self, valor):
        nodo = Nodo(valor)

        if self.cabeza:
            self.cabeza.sgte = nodo
            self.cabeza = nodo

        else:
            self.cabeza = nodo
            self.cola = nodo

    def recorrer(self):
        actual = self.cola
    
        while actual:
            valor = actual.valor
            actual = actual.sgte
            yield valor

    def eliminar(self, x):
        actual = self.cola
        anterior = self.cola

        while actual:
            if actual.valor == x:
                if actual == self.cola:
                    self.cola = actual.sgte

                else:
                    anterior.sgte = actual.sgte

                return
            anterior = actual
            actual = actual.sgte

    def buscar(self, valor):
        for val in self.recorrer():
            if val == valor:
                return True
            
            else:
                return False
    
    def cantidad(self):
        actual = self.cola
        cont = 0

        while actual:
            cont += 1
            actual = actual.sgte

        return cont

    def invertir(self):
        actual = self.cola
        anterior = None
        while actual:
            siguiente = actual.sgte
            actual.sgte = anterior
            anterior = actual
            actual = siguiente
        self.cola, self.cabeza = self.cabeza, self.cola


#Principal

#Cola
Q = Cola()
Q.agregar(1)
Q.agregar(2)
Q.agregar(3)
Q.agregar(4)
print(f"La cola invertida es: {Q.invertir()}")

#Pila
P = Pila()
P.apilar(1)
P.apilar(2)
P.apilar(3)
P.apilar(4)
P.apilar(5)
print(f"La pila invertida es: {P.invertir()}")

#Lista Enlazada
L = ListaEnlazada()
L.agregar(1)
L.agregar(2)
L.agregar(3)
L.agregar(4)
L.agregar(5)
L.agregar(6)

L.invertir()

print("La lista invertida es:")
for val in L.recorrer():
    print(val)