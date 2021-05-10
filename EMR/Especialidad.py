class Especialidad:
    def __init__(self,iE,nE,cE):
        self.idEspecialista = iE
        self.nombreEspecialidad = nE
        self.cantidadEspecialistas = cE

    def getidEspecialista(self):
        return self.idEspecialista

    def getNombreEspecialidad(self):
        return self.nombre

    # def cantidadEspecialistas(self):
    # return self.cantidadEspecialistas()
    def setidEspecialista(self, id):
        self.idEspecialista = id

    def setNombreEspecialidad(self, nom):
        self.nombre = nom

    def setcantidadEspecialistas(self, can):
        self.cantidadEspecialistas = can