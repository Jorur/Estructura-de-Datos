#Pregunta 2: Parcial2

def CrearM(m):
    matriz = []
    for i in range(m):
        a = [0] * m
        matriz.append(a)
    return matriz



def MatrizT(A):
    for i in range (len(A)):
        for j in range(len(A[0])):
            if j <= i: 
                A[i][j] = int(input("Elemento(%d,%d): "%(i, j))) 
    return A
            
        


def Vector(A):
    n = len(A)
    V = []
    for i in range(len(A)):
        for j in range (len(A[0])):
            if A[i][j] != 0:
                V.append(A[i][j])
    
    return V
    
def Valor(V, i, j):
    pos = 0
    for k in range(i+1):
        pos += k 
    pos += j 
    print("El valor en la posicion(%d,%d): "%(i,j),V[pos])
        
def maximo(V, i):
    A = []
    pos = int(i*(i+1)/2)# i es la longitud de la fila 
    for j in range(pos, pos+i+1):
        A.append(V[j])
    return max(A)

    
    


#Principal
B = CrearM(3)
B = MatrizT(B)
V = Vector(B)
print(V)
x = int(input("Ingrese i: "))
y = int(input("Ingrese j: "))
Valor(V, x, y)
i = int(input("Fila: "))
print(maximo(V, i))
