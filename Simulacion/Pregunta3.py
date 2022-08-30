#Pregunta 4: Simulacion

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
        
    
    


#Principal
A = [
    [1, 0, 0],
    [2, 3, 0],
    [4, 5, 6]
    ]

V = Vector(A)
x = int(input("Ingrese i: "))
y = int(input("Ingrese j: "))
Valor(V, x, y)
