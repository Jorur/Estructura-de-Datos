class Matriz:
    def __init__(self, m, n):
        self.filas = m
        self.columnas = n 
        self.matriz = []
        for i in range(self.filas):
            a = [0] * self.columnas
            self.matriz.append(a)

    def Llenar(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j] = int(input(f"Elemento({i},{j}): ")) 

    def Mostrar(self):
        for i in range(self.filas):
            print("[", end = "")
            for j in range(self.columnas):
                print("{:5s}".format(str(self.matriz[i][j])), end = "")
            print("]")

#Principal
Mat = Matriz(2, 2) 
Mat.Llenar()
Mat.Mostrar()




        
