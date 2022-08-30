class Pila:
    def __init__(self):
        self.elementos = []

    def agregar (self, valor):
        self.elementos.append(valor)

    def reemplazar (self, x, y):
        for i in range(len(self.elementos)):
            if self.elementos[i] == x:
                self.elementos[i] = y

#Pricipal
p = Pila()
p.agregar(1)
p.agregar(2)
p.agregar(3)
p.agregar(4)

print("Lista Vieja:")
for num in p.elementos:
    print(num)

p.reemplazar(3, 5)
print("Lista Nueva: ")

for num in p.elementos:
    print(num)
