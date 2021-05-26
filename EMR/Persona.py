class Persona:

    def __init__(self,n,r,s,d):
        self.nombre = n
        self.rut = r
        self.sexo = s
        self.direccion = d

    def setNombre(self, nombre):
        self.nombre = nombre

    def setRut(self, rut):
        self.rut = rut

    def setSexo(self, sexo):
        self.sexo = sexo

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getNombre(self):
        return self.nombre

    def getRut(self):
        return self.rut

    def getSexo(self):
        return self.sexo

    def getDireccion(self):
        return self.direccion

    def __str__(self):
        return self.nombre + "\n" + str(self.rut) + "\n" + self.sexo + "\n" + self.direccion