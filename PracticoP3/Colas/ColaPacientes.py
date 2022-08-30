class ColadePacientes:
    def __init__(self):
        self.cola = []

    def nuevo_paciente(self, nombre):
        self.cola.append(nombre)

    def proximo_paciente(self):
        return self.cola.pop(0)
    

class Recepcion:
    def __init__(self):
        self.consultorios = {"Dr. Rojas":None, "Dr. Urioste":None, "Dr. Nosborn":None}

    def nuevo(self, paciente, doctor):
        self.consultorios[doctor] = paciente

    def proximo(self, paciente, doctor):
        print(f" El paciente que ha salido es: {self.consultorios[doctor]}")
        self.consultorios[doctor] = paciente

#Principal
recep= Recepcion()

Q = ColadePacientes()
Q.nuevo_paciente("Jorge")
Q.nuevo_paciente("Mauricio")

Q1 = ColadePacientes()
Q1.nuevo_paciente("Jose mateo")
Q1.nuevo_paciente("Joaquin")

Q2 = ColadePacientes()
Q2.nuevo_paciente("Valeria")
Q2.nuevo_paciente("Micaela")

recep.nuevo(Q.proximo_paciente(),"Dr. Urioste")
print(recep.consultorios)

recep.nuevo(Q1.proximo_paciente(),"Dr. Rojas")
print(recep.consultorios)

recep.nuevo(Q2.proximo_paciente(),"Dr. Nosborn")
print(recep.consultorios)

recep.proximo(Q.proximo_paciente(),"Dr. Urioste")
print(recep.consultorios)


    
