def Suma(a, b):
    if b == 0:
        return a

    else:
        return Suma(a+1, b-1)

print(Suma(2, 2))