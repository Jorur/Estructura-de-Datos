#Crear una función recursiva para calcular la suma armónica.
# 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

def Armonica(n):
    if n < 2:
        return 1
    
    else:
        return 1/n + Armonica(n-1)

print(Armonica(7))