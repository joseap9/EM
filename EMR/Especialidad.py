class Especialidad:
    def __init__(self):
        self.idEspecialista = ""
        self.nombre = ""
        self.cantidadEspecialistas = 20

    def getidEspecialista(self):
        return self.idEspecialista

    def getnombre(self):
        return self.nombre

    # def cantidadEspecialistas(self):
    # return self.cantidadEspecialistas()
    def setidEspecialista(self, id):
        self.idEspecialista = id

    def setnombre(self, nom):
        self.nombre = nom

    def setcantidadEspecialistas(self, can):
        self.cantidadEspecialistas = can