from tkinter import *
from PIL import Image,ImageTk
from Medico import *
from Paciente import *
from Persona import *
from Especialidad import *
from functions import display_logo
#from SolicitarAtencion import *

#coloca boton dasboard



medico = Medico("","","","","","",20,"")
paciente = Paciente("","-","-","","","","","","")


listaTrauma = ListaTrauma([paciente])
listaNeuro = ListaNeuro([paciente])
listaCardio = ListaCardio([paciente])
listaCompleta = ListaCompleta([paciente])


def mostrarDatos(rut):
    
    frame = Frame(root, width=150,height=221, bg ="#909497")
    frame.place(x=404, y=200)
    Label(root, text = "Nombre",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=410,y=210)
    Label(root, text = "Rut",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=410,y=230)
    Label(root, text = "Sexo",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=410,y=250)
    Label(root, text = "Direccion",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=410,y=270)
    Label(root, text = "Diagnostico I.",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=410,y=290)
    Label(root, text = "Estado",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=410,y=320)
    Label(root, text = "Despacho",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=410,y=340)
    Label(root, text = "N° de Atencion",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=410,y=360)
    Label(root, text = "Cama Asig",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL SemiBold",12) ).place(x=410,y=380)
   

    #textBox muestra datos del paciente
    datosBox = Text(root,height = 8.5, width= 25, padx=15,pady=15, font=("Cascadia Code PL SemiBold",12) ,bg = "#B3B6B7", fg="#0026fe")
    datosBox.insert(1.0,rut)
    datosBox.place(x=554, y=200)




root = Tk()
root.title("Emergencias Medicas")

root.geometry("1200x500")


#encabezado -> logo
header = Frame(root, width = 1200, height = 160, bg = "white")
header.grid(columnspan = 5, row = 0)

#cuerpo
body = Frame(root, width = 1200, height = 340, bg = "#0026fe")
body.grid(columnspan = 5, row = 1)

#botones principales

#boton atencion
img = Image.open("images/SolicitarA.png")
img = ImageTk.PhotoImage(img)
agregar_btn = Button(root, image=img, borderwidth=0, command=lambda: ventanaAtencion())
agregar_btn.grid(column=1, row=0)

#boton medico esp
imgM = Image.open('images/medicoEsp.png')
imgM = ImageTk.PhotoImage(imgM)
agregar_medicoE = Button(root, image=imgM, borderwidth=0, command=lambda: ventanaMedicoEsp())
agregar_medicoE.grid(column=2, row=0)

#boton lista espera
imgI = Image.open('images/listaE.png')
imgI = ImageTk.PhotoImage(imgI)
listaE = Button(root, image=imgI, borderwidth=0, )
listaE.grid(column=3, row=0)


#Buscar Paciente

Label(root, text = "Buscar Paciente",bg="#0026fe",fg="white",height = 1,font=("Aharoni",12,'bold') ).place(x=92,y=200)
Label(root, text = "rut: ",bg="#0026fe",fg="white",height = 1,font=("Aharoni",12,'bold') ).place(x=45, y=270 )

#Buscar Paciente
buscaPaciente = StringVar()
buscaPaciente = Entry(root, width=25)
buscaPaciente.place(x=112,y=272)
#boton Datos paciente
txt = StringVar()



imgD = Image.open('images/DatosP.png')
imgD = ImageTk.PhotoImage(imgD)
buscarD = Button(root, image=imgD, borderwidth=0, bg="#0026fe", command=lambda: [ mostrarDatos(listaCompleta.buscar(buscaPaciente.get()))]  )
buscarD.place(x= 47, y= 346)

#boton estado paciente
img1 = Image.open('images/EstadoP.png')
img1 = ImageTk.PhotoImage(img1)
buscarE = Button(root, image=img1, borderwidth=0, bg="#0026fe",command=lambda: txt.set(listaTrauma.buscar(buscaPaciente.get())))
buscarE.place(x= 204, y= 346)

#textBox muestra datos del paciente
datosBox = Text(root,height = 8, width= 40, padx=15,pady=15, font=("Cascadia Code PL SemiBold",12), bg="#B3B6B7" , fg="black")
datosBox.insert(5.0,"Datos")
datosBox.place(x=404, y=200)



#boton Limpiar
imgL = Image.open('images/Limpiar.png')
imgL = ImageTk.PhotoImage(imgL)
limpiar = Button(root, image=imgL, borderwidth=0, bg="#0026fe", command =lambda: print(listaCompleta.mostrar())).place(x= 540, y= 435)


Label(root, text = "Prox. Paciente",bg="#0026fe",fg="white",height = 1,font=("Aharoni",12,'bold') ).place(x=918,y=250)

#textBox prox paciente
proxPacienteF = Frame(root, height = 65, width= 160, relief = "sunken", bg = "light grey").place(x=900, y=300)
muestra = Label(root,textvariable=txt,bg="#0026fe",fg="white",font=("Aharoni",12,'bold')).place(x=890, y=300)


#boton siguiente
imgS = Image.open('images/siguiente.png')
imgS = ImageTk.PhotoImage(imgS)
siguiente =Button(root, image=imgS, borderwidth=0, bg="#0026fe").place(x= 930, y= 400)

imgDb = Image.open('images/dashboard.png')
imgDb = ImageTk.PhotoImage(imgDb)
dashboard = Button(root, image=imgDb, borderwidth=0)
dashboard.place(x=1000,y=136)

display_logo('./images/logoucen.png',0,0)


def ventanaAtencion():

        def close_window(root):
            root.destroy()

        def listas(nombre,rut,sexo,direccion,diagI,estado,despacho):
    
            if despacho == "traumatologia":
                listaTrauma.agregar(Paciente(nombre,rut,sexo,direccion,diagI,estado,despacho,"",""))
            elif despacho == "neurologia":
                listaNeuro.agregar(Paciente(nombre,rut,sexo,direccion,diagI,estado,despacho,"",""))
            elif despacho == "cardiologia":
                listaCardio.agregar(Paciente(nombre,rut,sexo,direccion,diagI,estado,despacho,"","")) 

        
                

        root = Toplevel()
        root.title("Solicitar Atencion")
        root.geometry("450x350")

        sexos= ["masculino","femenino","otro"]
        estados=["reanimacion","emergencia","urgencia","prioritario","no urgencia"]
        #despachos=["traumatologia","neurologia","cardiologia"]
        

        #labels

        Label(root, text="Nombre:").place(x=40, y=30)
        nombre = Entry(root, width=40)
        nombre.focus()
        nombre.place(x=170,y=30)
        


        Label(root, text="rut:").place(x=40,y=60)
        rut = Entry(root, width=40)
        rut.place(x=170,y=60)

        Label(root, text="sexo:").place(x=40,y=90)
        sexo= Spinbox(root, values=sexos)
        sexo.place(x=170,y=90)


        Label(root, text="direccion:").place(x=40,y=120)
        direccion = Entry(root, width=40)
        direccion.place(x=170,y=120)

        #Label(root, text="cama Asignada:").grid(pady=5, row=4, column=0)
        #camaAsig = Entry(root, width=40)
        #camaAsig.grid(padx=5, row=4, column=1)

        Label(root, text="Diagnostico Inicial:").place(x=40,y=150)
        diagI = Entry(root, width=40)
        diagI.place(x=170,y=150)

        Label(root, text="estado:").place(x=40,y=180)
        estado = Spinbox(root, values=estados)
        estado.place(x=170,y=180)

        Label(root, text="despacho:").place(x=40,y=210)
    
        
        despacho = StringVar()
        trauma = Radiobutton(root,  text="Traumatologia",variable=despacho,value="traumatologia")
        trauma.place(x=170,y=210)
        trauma.select()

        neuro = Radiobutton(root,  text="Neurologia",variable=despacho,value="neurologia")
        neuro.place(x=170,y=230)

        cardio = Radiobutton(root,  text="Cardiologia", variable=despacho,value="cardiologia")
        cardio.place(x=170,y=250)

        
        

        #Label(root, text="numero de atencion:").grid(pady=5, row=6, column=0)
        #numAtencion = Entry(root, width=40)
        #numAtencion.grid(padx=5, row=6, column=1)

            

        agregar = Button(root, text="Agregar", width=50, command=lambda: [listas(nombre.get(),rut.get(),sexo.get(),direccion.get(),diagI.get(),estado.get(),despacho.get()), listaCompleta.agregar(Paciente(nombre.get(),rut.get(),sexo.get(),direccion.get(),diagI.get(),estado.get(),despacho.get(),"","")) ,close_window(root) ])
        agregar.place(x=50,y=300)

        

        #mostrar = Button(root, text="Listado de Pacientes", width=50, command=lambda: btnMostrar())
        #mostrar.grid(padx=10, pady=10, row=7, column=0, columnspan=2)
        #listaCompleta.agregar(Paciente(nombre.get(),rut.get(),sexo.get(),direccion.get(),diagI.get(),estado.get(),despacho.get(),"","")), listar.mostrar(),

        root.mainloop()

def ventanaMedicoEsp():

        cNom = StringVar()
        cRut = StringVar()
        cEstado = StringVar()
        cDiagI = StringVar()

        def close_window(root):
            root.destroy()


        def muestraEsp():

            if buscaP.get() == 'cardiologia':
                cNom.set(listaCardio.getNombre())
                cRut.set(listaCardio.getRut())
                cEstado.set(listaCardio.getEstado())
                cDiagI.set(listaCardio.getDiagnosticoI())
            elif buscaP.get() == 'traumatologia':
                cNom.set(listaTrauma.getNombre())
                cRut.set(listaTrauma.getRut())
                cEstado.set(listaTrauma.getEstado())
                cDiagI.set(listaTrauma.getDiagnosticoI())
            elif buscaP.get() == 'neurologia':
                cNom.set(listaNeuro.getNombre())
                cRut.set(listaNeuro.getRut())
                cEstado.set(listaNeuro.getEstado())
                cDiagI.set(listaNeuro.getDiagnosticoI())

            


        
        root = tk.Toplevel()
        root.title("Medico Especialista")
        root.geometry("550x500")

        #labels

        tk.Label(root, text="filtrar ", font=("Aharoni",10,'bold')).place(x=40,y=30)
        buscaP= StringVar()

        trauma = tk.Radiobutton(root, value='traumatologia', variable=buscaP, text='Traumatologia')
        trauma.place(x=100,y=30)
        trauma.select()

        neuro = tk.Radiobutton(root, value='neurologia', variable=buscaP, text='Neurologia')
        neuro.place(x=220,y=30)

        cardio = tk.Radiobutton(root, value='cardiologia', variable=buscaP, text='Cardiologia')
        cardio.place(x=320,y=30)

        tk.Button(root, text="ok", width=5,command = lambda: [muestraEsp()  ]).place(x=450,y=30)

        
        

        tk.Label(root, text="Nombre:").place(x=40, y=100)
        nombre = tk.Entry(root, width=40,state="readonly",textvariable=cNom)
        nombre.focus()
        nombre.place(x=170,y=100)
        

        
        tk.Label(root, text="Rut:").place(x=40,y=130)
        rut = tk.Entry(root, width=40,state="readonly",textvariable=cRut)
        rut.place(x=170,y=130)



        tk.Label(root, text="Diagnostico Inicial:").place(x=40,y=160)
        diagI = tk.Entry(root, width=40,state="readonly",textvariable=cDiagI)
        diagI.place(x=170,y=160)

        tk.Label(root, text="Estado:").place(x=40,y=190)
        estado = tk.Entry(root, width=40,state="readonly",textvariable=cEstado)
        estado.place(x=170,y=190)

        tk.Label(root, text="Diagnostico:").place(x=40,y=250)
        diagnostico = tk.Entry(root, width=40)
        diagnostico.place(x=170,y=250)

        tk.Label(root, text="Tratamiento:").place(x=40,y=280)
        tratamiento =  tk.Text(root, height = 5, width= 25, padx=15,pady=15)
        tratamiento.place(x=170,y=280)

        tk.Button(root, text = "llamar autoridades",width = 15).place(x=77, y=425)

        tk.Button(root, text = "alta medica",width = 10, command = lambda: [close_window(root)] ).place(x=250, y=425)

        tk.Button(root, text = "siguiente",width = 10).place(x=400, y=425)

        
        
        


        

        root.mainloop()






root.mainloop()

#agregar_btn = tk.Button(root, text="situacion de pacientes", font=("Aharoni",12,'bold'), bg="#0026fe", fg="white", height=1, width=18)
#otro = tk.Button(root, text="otro", font=("hp simplified",12), bg="#0026fe", fg="white", height=1, width=12,command=lambda:print("click"))
#otro.grid(column=1, row=0, pady=50, padx=100, )


#agregar_btn = tk.Button(root, text="lista de espera", font=("hp simplified",12), bg="#0026fe", fg="white", height=1, width=
#agregar_btn = tk.Button(root, image=display_btn('./images/btn_agregar.png',1,0,20,60,"nw"),borderwidth=0,command="click")





