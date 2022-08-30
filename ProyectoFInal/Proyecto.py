import time as t
import os
# -----------------------------------------------------------
class Arbol:
    def __init__(self, carga):
        self.carga = carga
        self.izquierda = None
        self.derecha = None

    def __str__(self):
        return str(self.carga)

# -----------------------------------------------------------

# Funciones
# -----------------------------------------------------------

def si(preg):
    resp = input(preg)
    return (resp.lower() == 'si')

# -----------------------------------------------------------

def main():
    bucle = True
    raiz = Arbol("pajaro")
    while bucle:
        if not si("Estas pensando en un animal? [si/no]: "): 
            break

        arbol = raiz
        while arbol.izquierda != None:
            if si(arbol.carga + "? "):
                arbol = arbol.izquierda
            else:
                arbol = arbol.derecha

        #adivinar
        animal = arbol.carga
        if si("Es un " + animal + "? "):
            print ("Animator gana otra vez B)")
            continue

        #obtener informacion
        nuevo = input("Qué animal era? ")
        info = input("Qué diferencia a un " + animal + " de un " + nuevo + "? ")
        indicador = "Si el animal fuera un " + animal + " cual seria la respuesta? "
        arbol.carga = info


        if si(indicador):
            arbol.izquierda = Arbol(animal)
            arbol.derecha = Arbol(nuevo)
        else:
            arbol.derecha = Arbol(animal)
            arbol.izquierda = Arbol(nuevo)
            
    os.system("CLS")
    return raiz

def Isleaf(raiz):
    return raiz.izquierda is None and raiz.derecha is None

def menu():
    print("Ingresa la opcion que desees:")
    print("1.- Empezar jugar")
    print("2.- Animales en el programa")
    print("3.- Creditos ")
    print("4.- Salir del juego")

def Recorrer(raiz):
    if raiz is not None:
        Recorrer(raiz.izquierda)
        if Isleaf(raiz):
            print(raiz)

        Recorrer(raiz.derecha)

def Contador(raiz):
    if raiz is not None:
        Contador(raiz.izquierda)

        if Isleaf(raiz):
            return 1 

        Contador(raiz.derecha)

    

        
        

#Principal
if __name__ == '__main__':
    print("------Akinator de animales------")
    print("Bienvenido al Adivinador de animales")
    nombre = input("Ingresa tu nombre: ")
    t.sleep(1)
    os.system('CLS')

    ciclo = True
    raiz = Arbol("pajaro")
    print(f"Hola, {nombre}, elige una opcion por favor:")
    print()
    while ciclo:
        menu()
        print()
        op = int(input("Ingrese la opcion que desea: "))
        os.system("CLS")
        if op ==1:
            raiz = main()

        elif op == 2:
            print("Los animales que hay son: ")
            Recorrer(raiz)
            t.sleep(5)
            os.system("CLS")
            

        elif op == 3:
            print("Este programa fue desarrollado por:")
            t.sleep(1)
            print("Oscar Aguilar")
            t.sleep(1)
            print("Nicole Numberg")
            t.sleep(1)
            print("Jorge Urioste")
            t.sleep(1)
            print("Brenda Villalobos")
            t.sleep(2)
            os.system('CLS')
            

        elif op == 4:
            print(f"Muchas gracias por jugar, {nombre}")
            print()
            print("Esperamos que te haya gustado...")
            ciclo = False

        elif op ==5:
            print(f"La cantidad de animales que hay en el sistema es:", Contador(raiz))
            

