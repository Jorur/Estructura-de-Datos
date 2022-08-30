class Pila:
    def __init__(self, n):
        self.tamano = n
        self.pila = [0] * (self.tamano + 1)
        self.top = 0 

    def Add (self, item):
        if self.top == self.tamano:
            print("La cola esta llena...")
        else:
            self.top += 1
            self.pila[self.top] = item

    def Del(self):
        if self.top == 0:
            print("La cola esta vacia...")

        else:
            self.pila[self.top] = 0
            self.top -= 1 

#Main
p1 = Pila(4) 
p1.Add(1) 
p1.Add(2)
p1.Add(3)
p1.Add(4)
for i in range(1, p1.tamano+1):
    print(p1.pila[i])

print("Top:",p1.pila[p1.top])
    

