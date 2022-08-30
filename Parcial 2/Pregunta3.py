#Pregunta 3 : intercambiar Filas



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

def LeeMatriz(A,):
    for i in range(len(A)):
        for j in range(len(A[i])):
            #A[i][j]=int(input("elemento:"))
            A[i][j]=int(input('Elemento: (%d,%d):'%(i, j)))
    return A
    
def Inter(A, i, i1):
        A[i], A[i1] = A[i1], A[i]
        
#principal
A = CreaMatriz(3, 3)
LeeMatriz(A)
ImprimaMat(A)
i = int(input("Ingrese el numero de la primera fila a intercambiar: "))
i1 = int(input("Ingrese el numero de la segunda fila a intercambiar: "))
Inter(A, i, i1)
ImprimaMat(A)
