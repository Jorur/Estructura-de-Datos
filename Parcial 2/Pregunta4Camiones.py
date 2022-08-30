#Pregunta 4 Fila 1: Camiones

def CrearP(n):
    Pila = [0]*(n+1)
    top = 0
    return Pila, top

def AgregarP(item, S, top):
    if top == len(S):
        print("La pila esta llena")
        
    else:
        top +=1
        S[top] = item
        return top
        
def EliminarP(S, top):
    if top == 0:
        print("La pila esta vacia")
        
    else:
        S[top] = 0
        top -= 1
        return top
        
def CrearC(n):
    Cola = [0] * (n+1)
    front = 0
    rear = 0
    return Cola, front, rear

def AgregarC(item, Q, r):
    if len(Q) == r:
        print("La cola esta llena...")
        
    else:
        r +=1
        Q[r] = item
        return r
    
#Principal
P, t = CrearP(4)
Q, f, r = CrearC(4)

for i in range  (4):
    item = input("Ingrese el numero de caja y Fecha de embalaje: ")
    t = AgregarP(item, P, t)
    
for i in range(4):
    r = AgregarC(P[t], Q, r)
    t = EliminarP(P, t)
print(Q)
    
    

    
