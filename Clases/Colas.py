class Cola:
    def __init__(self, n):
        self.tamano = n+1
        self.Cola = [0] * self.tamano
        self.front = 0
        self.rear = 0

    def Llenar(self, item):
        if self.tamano == self.rear:
            print("La cola esta Llena...")

        else:
            self.rear += 1
            self.Cola[self.rear] = item

    def Del(self):
        if self.front == self.rear:
            print("La cola esta vacia...")

        else:
            self.front += 1
            self.Cola[self.front] = None

#Principal
Q = Cola(4)
Q.Llenar(1)
Q.Llenar(2)
Q.Llenar(3)
Q.Llenar(4)

for i in range(1, Q.tamano):
    print(Q.Cola[i])

Q.Del()
print()

for i in range(1, Q.tamano):
    print(Q.Cola[i])

