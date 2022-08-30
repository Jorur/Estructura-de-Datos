from random import randint

def Experimento(numero):
    print(f"Camino: {numero}")
    if numero == 1:
        return 3 + Experimento(randint(1, 3))

    elif numero == 2:
        return 5 + Experimento(randint(1, 3))

    else:
        return 7

#main
print("El tiempo que tarda en salir es: ", Experimento(randint(1,3)))
