from tkinter import *
from PIL import Image,ImageTk
from Medico import *
from Paciente import *
from Persona import *
from Especialidad import *
from functions import display_logo




medico = Medico("","","","","","")
paciente = Paciente("","-","-","","","","","",""   ,"","","","","","")

# Lista de pacientes
listaTrauma = ListaTrauma([paciente])
listaNeuro = ListaNeuro([paciente])
listaCardio = ListaCardio([paciente])
listaCompleta = ListaCompleta([paciente])

listaTest = ListaEnlazada()


#Lista de medicos
#listaMedicosTrauma = ListaMedicosTrauma([medico])
#listaMedicosTrauma.agregar(Medico("alberto","26970671-6","M","las casas 83","001","Traumatologia",542))
medico = ["alberto","26970671-6","No disponible","No Disponible","543","Traumatologia"]

def bLimpiar():
    frame = Frame(root, width=410,height=221, bg ="#B3B6B7")
    frame.place(x=404, y=200)
    imgLim = Image.open("images/defLimpiar.png")
    imgLim = ImageTk.PhotoImage(imgLim)
    img_label = tk.Label(image = imgLim , bg="#B3B6B7")
    img_label.Image = imgLim
    img_label.place(x=404, y=200)

    



def mostrarEstado(rut,rutT, rutD):
    txt = StringVar()
    txt1 = StringVar()
    txt2 = StringVar()
    frame = Frame(root, width=410,height=221, bg ="#B3B6B7")
    frame.place(x=404, y=200)
    
    
    tMedico = Frame(root,width=413,height=30,bg="#909497" )
    tMedico.place(x=404,y=200)
    Label(root, text = "Medico Tratante",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL",12) ).place(x=530,y=202)
    mMedico = Label(root, textvariable= txt,bg = "#B3B6B7", fg="#0026fe",height = 1,font=("Cascadia Code PL",10) )
    mMedico.place(x=465,y=231)
    txt.set(rut)
    
    
    fDiagnostico = Frame(root,width=413,height=30,bg="#909497" )
    fDiagnostico.place(x=404,y=260)
    Label(root, text = "Diagnostico",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL",12) ).place(x=532,y=260)
    tdiagnostico = Label(root, textvariable= txt1,bg = "#B3B6B7", fg="#0026fe",height = 1,font=("Cascadia Code PL",10) )
    tdiagnostico.place(x=430,y=295)
    txt1.set(rutD)

    fTratamiento = Frame(root,width=413,height=30,bg="#909497" )
    fTratamiento.place(x=404,y=320)
    Label(root, text = "Tratamiento",bg = "#909497", fg="black",height = 1,font=("Cascadia Code PL",12) ).place(x=532,y=320)
    ttratamiento = Label(root, textvariable = txt2,bg = "#B3B6B7", fg="#0026fe",height = 1,font=("Cascadia Code PL",10) )
    ttratamiento.place(x=430, y=365)
    txt2.set(rutT)






    




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
    datosBox = Text(root,height = 8.5, width= 26, padx=15,pady=15, font=("Cascadia Code PL SemiBold",12) ,bg = "#B3B6B7", fg="#0026fe")
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
buscarD = Button(root, image=imgD, borderwidth=0, bg="#0026fe", command=lambda: [ mostrarDatos(listaCompleta.buscar(buscaPaciente.get())) ]  )
buscarD.place(x= 47, y= 346)

#boton estado paciente
img1 = Image.open('images/EstadoP.png')
img1 = ImageTk.PhotoImage(img1)
buscarE = Button(root, image=img1, borderwidth=0, bg="#0026fe",command=lambda:  [mostrarEstado(listaCompleta.buscarMedico(buscaPaciente.get()), listaCompleta.mostrarT(buscaPaciente.get()), listaCompleta.mostrarD(buscaPaciente.get()) ) , listaTest.imprimir()])
#txt.set(listaTrauma.buscar(buscaPaciente.get() )), listaTest.imprimir()
buscarE.place(x= 204, y= 346)

#muestra datos del paciente
imgLim = Image.open("images/defLimpiar.png")
imgLim = ImageTk.PhotoImage(imgLim)
img_label = tk.Label(image = imgLim , bg="#B3B6B7")
img_label.Image = imgLim
img_label.place(x=404, y=200)



#boton Limpiar
imgL = Image.open('images/Limpiar.png')
imgL = ImageTk.PhotoImage(imgL)
limpiar = Button(root, image=imgL, borderwidth=0, bg="#0026fe", command =lambda: bLimpiar() ).place(x= 540, y= 435)


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

        def distribuirListas(nombre,rut,sexo,direccion,diagI,estado,despacho):
            
            listaCompleta.agregar(Paciente(nombre,rut,sexo,direccion,diagI,estado,despacho,"",""    ,medico[0],medico[1],medico[2],medico[3],medico[4],medico[5]))
    
            if despacho == "traumatologia":
                listaTrauma.agregar(Paciente(nombre,rut,sexo,direccion,diagI,estado,despacho,"",""  ,"","","","","","" ))
            elif despacho == "neurologia":
                listaNeuro.agregar(Paciente(nombre,rut,sexo,direccion,diagI,estado,despacho,"","" ,"","","","","","" ))
            elif despacho == "cardiologia":
                listaCardio.agregar(Paciente(nombre,rut,sexo,direccion,diagI,estado,despacho,"",""    ,"","","","","","" )) 

        
                

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

            

        agregar = Button(root, text="Agregar", width=50, command=lambda: [listaTest.encolar(Paciente(nombre.get(),rut.get(),sexo.get(),direccion.get(),diagI.get(),estado.get(),despacho.get(),"",""   ,"","","","","","" )),    distribuirListas(nombre.get(),rut.get(),sexo.get(),direccion.get(),diagI.get(),estado.get(),despacho.get()), close_window(root)   ])
        agregar.place(x=50,y=300)

        

        #mostrar = Button(root, text="Listado de Pacientes", width=50, command=lambda: btnMostrar())
        #mostrar.grid(padx=10, pady=10, row=7, column=0, columnspan=2)
        #listaCompleta.agregar(Paciente(nombre.get(),rut.get(),sexo.get(),direccion.get(),diagI.get(),estado.get(),despacho.get(),"","")), listar.mostrar(),
                                    #nombre,rut,sexo,direccion,diagI,estado,despacho,"","" 
        root.mainloop()

def ventanaMedicoEsp():

        cNom = StringVar()
        cRut = StringVar()
        cEstado = StringVar()
        cDiagI = StringVar()
        rutP = StringVar()
        tratamiento = StringVar()
        diagnostico = StringVar()

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
        rutP = tk.Entry(root, width=40,state="readonly",textvariable=cRut)
        rutP.place(x=170,y=130)



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

        tk.Button(root, text = "alta medica",width = 15, command = lambda: listaCompleta.setTratamiento(tratamiento.get("1.0","end"))).place(x=77, y=425)

        tk.Button(root, text = "actualizar",width = 10, command = lambda: [listaCompleta.actualizaT(rutP.get(),tratamiento.get("1.0","end")), listaCompleta.actualizaD(rutP.get(),diagnostico.get()) ] ).place(x=250, y=425)

        tk.Button(root, text = "siguiente",width = 10).place(x=400, y=425)

        
        
        


        

        root.mainloop()






root.mainloop()





