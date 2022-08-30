class ColadePostulantes:
    def __init__(self):
        self.postulantes = []

    def nuevo_postulante(self, nombre):
        self.postulantes.append(nombre)

    def proximo_postulante(self):
        return self.postulantes.pop(0)

class Entrevista:
    def __init__(self):
        self.personas = {}

    def nuevo_postulante(self, postulante, entrevistador, sala):
        self.personas[entrevistador + str(sala)] = postulante

    def proximo_postulante(self, postulante, entrevistador, sala):
        print(f"El postulante que ha salido es {self.personas[entrevistador+ str(sala)]}")
        self.personas[entrevistador + str(sala)] = postulante