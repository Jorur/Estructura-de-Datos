#Pregunta 6: Estudiantes

def CrearC(n):
    Q = [0]*(n+1)
    front = 0 
    rear = 0 
    return Q, front, rear 

def AddC(item, Q, rear):
    if rear == len(Q):
        print("La Cola esta llena.")
        
    else:
        rear += 1 
        Q[rear] = item
        
    return rear
    
def Bubble(A, n, B):
    for  k in range(1, n):
        for i in range(1, n-k):
            if A[i] < A[i+1]:
                aux = A[i]
                aux1 = B[i]
                
                A[i] = A[i+1]
                B[i] = B[i+1]
                
                A[i+1] = aux
                B[i+1] = aux1


#Principal
n = 4000
estudiantesd = 6*8
dias = 4000/estudiantesd
dias = round(dias, 2)
print("La cantidad de Dias es: ", dias)

Nombres,f, r = CrearC(6)
Nota,f1, r1 = CrearC(6)

for i in range(1, 7):
    x = input("Ingrese el nombre: ")
    y = int(input("Ingrese la nota: "))
    r =AddC(x, Nombres, r)
    r1 =AddC(y, Nota, r1)
    
print()
 
for i in range (1, 7):
    print(Nombres[i], Nota[i])
    
Bubble(Nota, len(Nota), Nombres)

print()
print("Cola ordenanda")
for i in range (1, 7):
    print(Nombres[i], Nota[i])   

    







