class Carta:
    def __init__ (self, valor, palo):
        self.valor = valor
        self.palo = palo

    def __str__ (self):
        return f'{self.valor}, {self.palo}'

class PiladeCartas:
    def __init__ (self):
        self.cartas = []
        self.top = None

    def agregar (self, valor, palo):
        carta = Carta(valor, palo)

        if len(self.cartas) == 0:
            self.cartas.append(carta)
            self.top = carta

        elif carta.valor < self.top.valor and carta.palo != self.top.palo:
            self.cartas.append(carta)
            self.top = carta

        else:
            print(f"No se puede apilar...{carta.valor}, {carta.palo}")

  

#Principal
p1 = PiladeCartas()
p1.agregar(10, "Espada")
p1.agregar(5, "Corazon")
p1.agregar(7, "Diamante")
p1.agregar(3, "Corazon")

print("Las Cartas en la pila son:")
for car in p1.cartas:
    print(car)




        

    
