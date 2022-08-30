#Pregunta 4: Interacalar los nombres de dos vectores en una cola


def CrearC(n):
    Cola = [0] *(n+1)
    front = 0
    rear = 0
    return Cola, front, rear
    
def AddC(item, Q, rear):
    if rear == len(Q):
        print("La cola esta llena... ")
        
        
    else:
        rear += 1 
        Q[rear] = item
        
        
    return rear
    



#Principal
a = ["Juan 76", "Pedro 40", "Maria 55", "Rene 62", "Joaquin 23"]
b = ["Roberto 48", "Luis 65", "Marioly 70", "Ana Maria 55", "Andres 25", "Ana Julia 22"]
aux = []
Q, f, r = CrearC(len(a)+len(b))
n = len(Q)
for j in range(len(a), len(b)):
    aux.append(b[j])

cont = 0
for i in range (len(a)):
    r = AddC(a[i],Q, r)
    r = AddC(b[i],Q, r)
    cont += 1

cont *= 2

l = 0
for k in range (cont+1, n):
    r = AddC(aux[l],Q, r)
    l += 1

for i in range(1, n):
    print(Q[i])