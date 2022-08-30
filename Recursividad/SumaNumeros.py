#Crear función recursiva para sumar los valores n+(n-2)+(n-4) hasta n-x <= 0

def SumaValores(n):
    if n < 1:
        return 0

    else:
        return n + SumaValores(n-2)

print(SumaValores(8))