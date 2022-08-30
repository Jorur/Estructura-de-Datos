#Pregunta 1 examen2: Eliminar Elemento de cola

def CrearC(n):
    Cola = [0] *(n+1)
    front = 0
    rear = 0
    return Cola, front, rear
    
def AddC(item, Q, rear, n):
    if rear == n:
        print("La cola esta llena... ")
        
        
    else:
        rear += 1 
        Q[rear] = item
        
        
    return rear
        
def DeleteC(Q):
    aux = []
    aux1 = []
    n = len(Q)
    x = int(input("Valor: "))
    j = BinSrch(Q, x)
    for i in range(1, j):
        aux.append(Q[i])

    for k in range(j+1, n):
        aux1.append(Q[k])
    
    aux += aux1

    Q[1] = Q[j]
    cont = 0   
    for l in range(2, n):
        Q[l] = aux[cont]
        cont +=1
    

    
def BinSrch(A,x):
    n = len(A)
    lower = 0
    upper = n
    j = -1
    while lower <= upper:
        medio = (lower+upper)//2
       
        if x > A[medio]:
            lower = medio + 1

        elif x < A[medio]:
            upper = medio - 1

        else:
            j = medio
            return j  
    return j
       

#Principal
n = 4
Q, f, r = CrearC(n)
r =AddC(1, Q, r, n)
r =AddC(2, Q, r, n)
r =AddC(3, Q, r, n)
r =AddC(4, Q, r, n)
print(Q)
DeleteC(Q)
print(Q)