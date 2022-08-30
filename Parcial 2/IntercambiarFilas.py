def CreaMatriz(m,n):
    matriz=[]
    for i in range(m):
        a=[0]*n
        matriz.append(a)
    return matriz


def ImprimaMat(X):
    for i in range(len(X)):
        print('[',end="")
        for j in range(len(X[0])):
            print('{:5s}'.format(str(X[i][j])),end=""),
            #print(format((X[i][j])),"  ",end=""),
        print (']')

def LeeMatriz(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            #A[i][j]=int(input("elemento:"))
            A[i][j]=int(input('Elemento: (%d,%d):'%(i, j)))
    return A

def Inter(A, fila1, fila2):
    aux = A[fila1]
    aux1 = A[fila2]
    A[fila1] = aux1
    A[fila2] = aux

#Principal
A = CreaMatriz(3, 3)
LeeMatriz(A)
ImprimaMat(A)
print()
Inter(A, 1, 0)
ImprimaMat(A)
