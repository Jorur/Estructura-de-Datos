class Pila:
    def __init__ (self):
        self.elementos = []
    
    def Apilar(self, valor ):
        self.elementos.append(valor)

    def Desapilar(self):
        self.elementos.pop()

    def Vacio(self):
        return len(self.elementos) == 0

    def top(self):
        return self.elementos[-1]

#Implementando

S = Pila()

#Verificar si la cola esta vacia
print(S.Vacio())

S.Apilar(1)
S.Apilar(2)
S.Apilar(3)
S.Apilar(4)
S.Apilar(5)

#Mostrar Pila
print(S.elementos)

#Mostrar top
print("Top:", S.top())

#Verificar si la cola esta vacia
print(S.Vacio())

#Eliminar Valores de la pila
S.Desapilar()
S.Desapilar()
S.Desapilar()
S.Desapilar()
S.Desapilar()

#Verificar si la cola esta vacia
print(S.Vacio())


    
