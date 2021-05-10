from Persona import *
from Especialidad import *
from Paciente import *
import tkinter as tk


class Medico( Persona,Especialidad ):

    def __init__(self,nombre,rut,sexo,direccion,idEspecialista,nombreEspecialidad,cantidadEspecialistas,idMedico):

        Persona.__init__(self,nombre,rut,sexo,direccion)
        Especialidad.__init__(self,idEspecialista,nombreEspecialidad,cantidadEspecialistas)
        self.idMedico=idMedico





    def getIdMedico(self):
        return self.idMedico

    def setIdMedico(self,idMedico):
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

    def ventanaMedicoEsp(self):

        def close_window(root):
            root.destroy()
        
        root = tk.Tk()
        root.title("Medico Especialista")
        root.geometry("550x500")

        #labels

        tk.Label(root, text="filtrar ", font=("Aharoni",10,'bold')).place(x=40,y=30)
        buscaP= tk.StringVar()
        tk.Radiobutton(root, value="Traumatologia", variable=buscaP, text="Traumatologia").place(x=100,y=30)
        tk.Radiobutton(root, value="neurologia", variable=buscaP, text="neurologia").place(x=220,y=30)
        tk.Radiobutton(root, value="cardiologia", variable=buscaP, text="cardiologia").place(x=320,y=30)
        tk.Button(root, text="ok", width=5).place(x=450,y=30)

        tk.Label(root, text="Nombre:").place(x=40, y=100)
        nombre = tk.Entry(root, width=40,state="readonly")
        nombre.focus()
        nombre.place(x=170,y=100)
        


        tk.Label(root, text="Rut:").place(x=40,y=130)
        rut = tk.Entry(root, width=40,state="readonly")
        rut.place(x=170,y=130)



        tk.Label(root, text="Diagnostico Inicial:").place(x=40,y=160)
        diagI = tk.Entry(root, width=40,state="readonly")
        diagI.place(x=170,y=160)

        tk.Label(root, text="Estado:").place(x=40,y=190)
        estado = tk.Entry(root, width=40,state="readonly")
        estado.place(x=170,y=190)

        tk.Label(root, text="Diagnostico:").place(x=40,y=250)
        diagnostico = tk.Entry(root, width=40)
        diagnostico.place(x=170,y=250)

        tk.Label(root, text="Tratamiento:").place(x=40,y=280)
        tratamiento =  tk.Text(root, height = 5, width= 25, padx=15,pady=15)
        tratamiento.place(x=170,y=280)

        tk.Button(root, text = "llamar autoridades",width = 15).place(x=77, y=425)

        tk.Button(root, text = "alta medica",width = 10, command = lambda: close_window(root) ).place(x=250, y=425)

        tk.Button(root, text = "siguiente",width = 10).place(x=400, y=425)

        
        
        


        

        root.mainloop()