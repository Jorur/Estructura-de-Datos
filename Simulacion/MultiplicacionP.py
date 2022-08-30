#Multiplicacion de polinomios

def Multiplicacion(poly1, poly2):
    R = {}
    aux = {}
    for e1 in poly1:
        for e2 in poly2:
            R[e1+e2] = 0
    print(R)       
    for e1 in poly1:
        for e2 in poly2:
            aux[e1+e2] = poly1[e1] * poly2[e2]
            
        for ef in R:
            for ea in aux:
                if ef == ea:
                    R[ef] += aux[ea]
        aux = {}            
    print(R)
                    
#Principal
P = {4: 4, 2: 7, 0: 5}
Q = {5: 2, 3: 5, 1: 2}
Multiplicacion(P, Q)
    
