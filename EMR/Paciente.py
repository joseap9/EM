from Persona import *
import tkinter as tk

listaPacientes = []

class Paciente(Persona):

    def __init__(self,nombre,rut,sexo,direccion,diagnosticoI,estado,despacho,camaAsig,numeroDeAtencion):
        super().__init__(nombre,rut,sexo,direccion)
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



    def buscaPorRut(self,rut):
        
        for x in range(len(listaPacientes)):
            if listaPacientes[x].getRut == rut:
                listaPacientes[x].muestra()

            else:
                print("FAIL")

    def __str__(self):
        return super().__str__() + "\n"  + "diagnostico Inicial: " + self.diagnosticoI + "\n" + "estado: "+ self.estado + "\n" + "despacho: "+ self.despacho+"\n" + "num de atencion" + str(self.numeroDeAtencion) + "\n" + "cama asig" +str(self.camaAsig)+"\n======================="
    
    
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





    











    
