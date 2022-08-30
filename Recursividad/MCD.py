# Crear una función recursiva para calcular el máximo común divisor (MCD).

def MCD(a, b):
    minimo = min(a, b)
    maximo = max(a, b)

    if minimo == 0:
         return maximo

    elif minimo == 1:
        return 1

    else:
        return MCD(minimo, maximo % minimo)

print(MCD(50, 75))