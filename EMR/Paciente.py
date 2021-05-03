
from Persona import *

listaPacientes = []

class Paciente(Persona):

    def __init__(self,nombre,edad,sexo,direccion,estado,camaAsig,numeroDeAtencion):
        super().__init__(nombre,edad,sexo,direccion)
        self.estado = estado
        self.camaAsig = camaAsig
        self.numeroDeAtencion = numeroDeAtencion
        # self.medicoTratante= #medico especialista podemos sacarlo del area y buscar el primer
        # medico que posea esta, deberia ser un afuncion la cual ejecutemos aqui
        # self.medicoPrioridad=#primer medico que lo atiende


    def solicitarAtencion(self,nombre,edad,sexo,direccion, estado, camaAsig, numAtencion):
        nuevoPaciente = Paciente(nombre,edad,sexo,direccion,estado,camaAsig,numAtencion)
        listaPacientes.append(nuevoPaciente)

        n = 1
        for x in range(len(listaPacientes)):
            if len(listaPacientes) == n:
                print("agregado")
                print("hay ", n, "pacientes agregados")
            n = n + 1

    def muestra(self):
        for x in range(len(listaPacientes)):
            print(listaPacientes[x].__str__())

    def __str__(self):
        return super().__str__() + "\n" + str(self.camaAsig) + "\n" + self.estado + "\n" + str(self.numeroDeAtencion)

    def getestado(self):
        return self.estado

    def getcamaAsig(self):
        return self.camaAsig

    def getnumeroDeAtencion(self):
        return self.numeroDeAtencion

    def getmedicoTratante(self):
        return self.medicoTratante

    def getmedicoPrioridad(self):
        return self.medicoPrioridad

    def setestado(self, estado):
        self.estado = estado

    def setcamaAsig(self, camaAsig):
        self.camaAsig = camaAsig

    def setnumeroDeAtencion(self, n):
        self.numeroDeAtencion = n

    def setmedicoTratante(self, medico):
        self.medicoTratante = medico

    def setmedicoPrioridad(self, prioridad):
        self.medicoPrioridad = prioridad

    def asigPrioridadPaciente(self, listadoDePacientes, prioridad):
        if prioridad == 1:
            # agregar a listadoDePacientes
            print("")
        elif prioridad == 2:
            # agregar a listadoDePacientes
            print("")
        elif prioridad == 3:
            # agregar a listadoDePacientes
            print("")

    def estadoPaciente(self):
        # mostrar si se encuentra internado o no (puede ser comparardo su rut con la lista de pacientes y si pocee cama)
        # asi identificamos si esta en espera, tratamiento o sin ser atendido
        print("")

    def mostrarPacienteEspecialidad(self):
        # no entiendo que hace esta funcion....
        print("")

    def dashboardPacientes(self, listadoDePacientes):
        # for i=0;i++;i=lend(listadoDePacientes):
        # print(listadoDePacientes[i])
        print("")

    def despacharEspecialidad(self):
        # nose si espara llevarlo a un area o sacarlo de ahi
        print("")
