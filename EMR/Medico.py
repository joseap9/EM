from Persona import *


class Medico( Persona ):

    def __init__(self,idMedico):
        self.idMedico=idMedico


    def getidMedico(self):
        return self.idMedico

    def setidMedico(self,idMedico):
        self.idMedico=idMedico


    #def altamedica(self,listaPacienteConCama,paciente):
        #devera eliminar de una lista de pacientes al paciente ingresado

    #def indicarTratamiento(self,listaPacienteConCama):
        #quedara porvesre que hace este elemento o si seguira dentro de medico

    #def diasnoticar(self,listaPacienteConCama):
        #metodo de selecion de area para un paciente

    #esta funcion deveria ser ejecutada fuera de la clase medico ya que estariamos adcediendo a un valor que se
    #creara un aves creado los medicos
    #def morbilidad(self):
        #self.morbilidad = persona.getarea()

    def activarAutoridades(self,respuesta):
        if respuesta=="si":
            return "llamando al 133"

    #deveria ser una funcion y no un contenido de la clase
    #def mostrarMedico(self,listadoDeMedicos):
        #buscar medico por el rut del medico