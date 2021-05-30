from Medico import *
from Persona import *
from Nodo import *
import tkinter as tk



class Paciente( Persona, Medico) :

    def __init__(self,nombre,rut,sexo,direccion,diagnosticoI,estado,despacho,camaAsig,numeroDeAtencion, nombreM,rutM,diagnostico,tratamiento,idEspecialista,nombreEspecialidad):
        Persona.__init__(self,nombre,rut,sexo,direccion)
        Medico.__init__(self,nombreM,rutM,diagnostico,tratamiento,idEspecialista,nombreEspecialidad)
        self.estado = estado
        self.camaAsig = camaAsig
        self.numeroDeAtencion = numeroDeAtencion
        self.diagnosticoI=diagnosticoI
        self.despacho = despacho
        

    def getEstado(self):
        return self.estado

    def getCamaAsig(self):
        return self.camaAsig

    def getNumeroDeAtencion(self):
        return self.numeroDeAtencion
    
    def getDespacho(self):
        return self.despacho

    def getDiagnosticoI(self):
        return self.diagnosticoI
    

    def setEstado(self, estado):
        self.estado = estado

    def setCamaAsig(self, camaAsig):
        self.camaAsig = camaAsig

    def setNumeroDeAtencion(self, n):
        self.numeroDeAtencion = n

    def setDiagnosticoI(self,d):
        self.diagnosticoI = d
    
    def setDespacho(self, des):
        self.despacho = des

    
    
    def solicitarAtencion(self,nombre,rut,sexo,direccion,diagnosticoI, estado, despacho, camaAsig, numAtencion):
        nuevoPaciente = Paciente(nombre,rut,sexo,direccion,diagnosticoI,estado,despacho,camaAsig,numAtencion)
        self.listaPacientes.append(nuevoPaciente)

        n = 1
        for x in range(len(self.listaPacientes)):
            if len(self.listaPacientes) == n:
                print("agregado")
                print("hay ", n, "pacientes agregados")
            n = n + 1

    def muestra(self):
        for x in range(len(self.listaPacientes)):
            return self.listaPacientes[x].__str__()

    
    def __str__(self):
        return Persona.__str__(self) + "\n" + self.diagnosticoI + "\n" + self.estado + "\n" + self.despacho+"\n" + str(self.numeroDeAtencion) + "\n" + str(self.camaAsig)+"\n==================================="
    


class ListaTrauma:

    listaPacientes = []  # Esta lista contendrá objetos de la clase Paciente

    def __init__(self, listaPacientes=[]):
        self.paciente = listaPacientes  

    def getNombre(self):
        for paciente in self.listaPacientes:
            return paciente.getNombre()

    def getRut(self):
        for paciente in self.listaPacientes:
            return paciente.getRut()
    
    def getEstado(self):
        for paciente in self.listaPacientes:
            return paciente.getEstado()

    def getDiagnosticoI(self):
        for paciente in self.listaPacientes:
            return paciente.getDiagnosticoI()
    

    def agregar(self, paciente):  
        self.listaPacientes.append(paciente)

    def mostrar(self):
        for paciente in self.listaPacientes:
            print(paciente)
        return "no hay pacientes"

    def buscar(self, rut):
        for paciente in self.listaPacientes:
            if paciente.getRut() == rut:
                return paciente
        return "Paciente no registrado"


class ListaCardio:

    listaPaciente = []  # Esta lista contendrá objetos de la clase Paciente

    def __init__(self, listaPaciente=[]):
        self.paciente = listaPaciente       

    def agregar(self, paciente):  
        self.listaPaciente.append(paciente)

    def mostrar(self):
        for paciente in self.listaPaciente:
            return paciente

    def getNombre(self):
        for paciente in self.listaPaciente:
           return paciente.getNombre()
    
    def getRut(self):
        for paciente in self.listaPaciente:
           return paciente.getRut()
    
    def getEstado(self):
        for paciente in self.listaPaciente:
           return paciente.getEstado()

    def getDiagnosticoI(self):
        for paciente in self.listaPaciente:
           return paciente.getDiagnosticoI()

    def buscar(self, rut):
        for paciente in self.listaPaciente:
            if paciente.getRut() == rut:
                return paciente
        return "Paciente no registrado"


class ListaCompleta():

    listaPacientes = []  # Esta lista contendrá objetos de la clase Paciente

    def __init__(self, listaPacientes=[]):
        self.paciente = listaPacientes 

    def getNombre(self):
        for paciente in self.listaPacientes:
            return paciente.getNombre()

    def getRut(self):
        for paciente in self.listaPacientes:
            return paciente.getRut()
    
    def getEstado(self):
        for paciente in self.listaPacientes:
            return paciente.getEstado()

    def getDiagnosticoI(self):
        for paciente in self.listaPacientes:
            return paciente.getDiagnosticoI() 

    def getTratamiento(self):
        for paciente in self.listaPacientes:
            return paciente.getTratamiento() 

    def setTratamiento(self,t):
        for paciente in self.listaPacientes:
            paciente.setTratamiento(t)


    def agregar(self, paciente):  
        self.listaPacientes.append(paciente)

    def mostrar(self):
        
        for paciente in self.listaPacientes:
            print(paciente)


    def buscar(self, rut):
        for paciente in self.listaPacientes:
            if paciente.getRut() == rut:
                return paciente
        return "Paciente no registrado"

    def buscarMedico(self, rut):

        for paciente in self.listaPacientes:
            if paciente.getRut() == rut:
                return paciente.muestraMedicoE()
               
        return "Paciente no registrado"

    
    def actualizaTk(self, rut, tratamiento):
        for paciente in self.listaPacientes:
            if rut == paciente.getRut():
                paciente.setTratamiento(tratamiento)
                
            else:
                paciente.setTratamiento("no disponible")

        
        
                

    def mostrarT(self, rut):
        
        for paciente in self.listaPacientes:
            if rut == paciente.getRut():
                return paciente.getTratamiento()
            
            
            
    def actualizaT(self, rut, tratamiento):

        for paciente in self.listaPacientes:
            if rut == paciente.getRut():
                paciente.setTratamiento(tratamiento)
            paciente.setRut(rut) 

    def mostrarD(self, rut):
        
        for paciente in self.listaPacientes:
            if rut == paciente.getRut():
                return paciente.getDiagnostico()
            
            
            
    def actualizaD(self, rut, diagnostico):

        for paciente in self.listaPacientes:
            if rut == paciente.getRut():
                paciente.setDiagnostico(diagnostico)
            paciente.setRut(rut) 

    
                


        
        
        



class ListaNeuro:

    listaPaciente = []  # Esta lista contendrá objetos de la clase Paciente

    def __init__(self, listaPaciente=[]):
        self.paciente = listaPaciente

    def getNombre(self):
        for paciente in self.listaPaciente:
            return paciente.getNombre()
    
    def getRut(self):
        for paciente in self.listaPaciente:
            return paciente.getRut()
        
    def getEstado(self):
        for paciente in self.listaPaciente:
            return paciente.getEstado()

    def getDiagnosticoI(self):
        for paciente in self.listaPaciente:
            return paciente.getDiagnosticoI() 
    

    def agregar(self, paciente):  
        self.listaPaciente.append(paciente)

    def mostrar(self):
        for paciente in self.listaPaciente:
            return paciente
        return ""

    def buscar(self, rut):
        for paciente in self.listaPacientes:
            if paciente.getRut() == rut:
                return paciente
        return "Paciente no registrado"

class ListaEnlazada:
    
    #_______________________________________________

    def __init__(self):
        # En el primer momento, tanto el primero como el último son None
        self.primero = None
        self.ultimo = None

    #_______________________________________________
    
    def encolar(self, x):
        nuevo = Nodo(x)
        # Si ya hay un último, agrega el nuevo y cambia la referencia.
        if self.ultimo:
            self.ultimo.prox = nuevo
            self.ultimo = nuevo
        # Si la cola estaba vacía, el primero es también el último.
        else:
            self.primero = nuevo
            self.ultimo = nuevo


    def imprimir(self):
        Nodo = self.primero
        while Nodo != None:
            print(Nodo.data, end = "\n")
            Nodo = Nodo.proximo

    def buscarPorRut(self,rut):
        Nodo = self.primero
        while Nodo != None:
            if Nodo.data.getRut() == rut:
                return Nodo.data
            Nodo = Nodo.proximo
        return "paciente no registrado"

    #_______________________________________________
        
    def desencolar(self):
        # Si hay un nodo para desencolar
        if self.primero:
            valor = self.primero.dato
            self.primero = self.primero.prox
        # Si después de avanzar no quedó nada, también hay que
        # eliminar la referencia del último.
        if not self.primero:
            self.ultimo = None
            return valor
        else:
            raise ValueError("La cola está vacía")
#_______________________________________________
        
    def es_vacia(self):
          return self.items == []

    


    






def ventanaAtencion(self):

        def close_window(root):
            root.destroy()

        sexos= ["masculino","femenino","otro"]
        estados=["reanimacion","emergencia","urgencia","prioritario","no urgencia"]
        #despachos=["traumatologia","neurologia","cardiologia"]
        root = tk.Tk()
        root.title("Solicitar Atencion")
        root.geometry("450x350")

        #labels

        tk.Label(root, text="Nombre:").place(x=40, y=30)
        nombre = tk.Entry(root, width=40)
        nombre.focus()
        nombre.place(x=170,y=30)
        


        tk.Label(root, text="rut:").place(x=40,y=60)
        rut = tk.Entry(root, width=40)
        rut.place(x=170,y=60)

        tk.Label(root, text="sexo:").place(x=40,y=90)
        sexo= tk.Spinbox(root, values=sexos)
        sexo.place(x=170,y=90)


        tk.Label(root, text="direccion:").place(x=40,y=120)
        direccion = tk.Entry(root, width=40)
        direccion.place(x=170,y=120)

        #tk.Label(root, text="cama Asignada:").grid(pady=5, row=4, column=0)
        #camaAsig = tk.Entry(root, width=40)
        #camaAsig.grid(padx=5, row=4, column=1)

        tk.Label(root, text="Diagnostico Inicial:").place(x=40,y=150)
        diagI = tk.Entry(root, width=40)
        diagI.place(x=170,y=150)

        tk.Label(root, text="estado:").place(x=40,y=180)
        estado = tk.Spinbox(root, values=estados)
        estado.place(x=170,y=180)

        tk.Label(root, text="despacho:").place(x=40,y=210)
        despacho= tk.StringVar()
        tk.Radiobutton(root, variable=despacho, text="Traumatologia",value="Traumatologia").place(x=170,y=210)
        tk.Radiobutton(root, variable=despacho, text="neurologia",value="neurologia").place(x=170,y=230)
        tk.Radiobutton(root, variable=despacho, text="cardiologia", value="cardiologia").place(x=170,y=250)
        

        #tk.Label(root, text="numero de atencion:").grid(pady=5, row=6, column=0)
        #numAtencion = tk.Entry(root, width=40)
        #numAtencion.grid(padx=5, row=6, column=1)

        agregar = tk.Button(root, text="Agregar", width=50, command=lambda: [self.solicitarAtencion(nombre.get(),rut.get(),sexo.get(),direccion.get(),diagI.get(),estado.get(),despacho.get(),"",""), self.muestra(),close_window(root)])
        agregar.place(x=50,y=300)

        #mostrar = tk.Button(root, text="Listado de Pacientes", width=50, command=lambda: btnMostrar())
        #mostrar.grid(padx=10, pady=10, row=7, column=0, columnspan=2)

        root.mainloop()





    











    
