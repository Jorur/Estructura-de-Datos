def metodo1(n):
    if n == 0:
        print('En método 1 con N:', n)
    else:
        metodo2(n)
def metodo2(n):
    print('En metodo 2 con N:', n)
    metodo3(n-1)
def metodo3(n):
    print('En metodo 3 con N:', n)
    metodo1(n-1)

metodo1(8)