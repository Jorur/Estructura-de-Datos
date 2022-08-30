#Crear una función recursiva para calcular la potencia de un número.
# a^b = a_1 * a_2 * a_3 * ... * a_b

def Pot(a, b):
    if b == 0:
        return 1

    elif a == 0:
        return 0

    elif b == 1:
        return a

    else:
        return a * Pot(a, b-1)

print(Pot(4, 3))