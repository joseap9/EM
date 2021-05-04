import tkinter as tk
from PIL import Image,ImageTk
from Medico import *
from Paciente import *
from Persona import *
from Especialidad import *
from functions import display_logo,display_btnn
from SolicitarAtencion import ventanaAtencion


root = tk.Tk()
root.title("Emergencias Medicas")

root.geometry("1200x500")


#encabezado -> logo
header = tk.Frame(root, width = 1200, height = 160, bg = "white")
header.grid(columnspan = 5, row = 0)

#cuerpo
body = tk.Frame(root, width = 1200, height = 340, bg = "#0026fe")
body.grid(columnspan = 5, row = 1)

#botones principales

#boton atencion
img = Image.open('images/SolicitarAten.png')
img = ImageTk.PhotoImage(img)
agregar_btn = tk.Button(root, image=img, borderwidth=0, command=lambda: ventanaAtencion())
agregar_btn.grid(column=1, row=0)

#boton medico esp
imgM = Image.open('images/medicoEsp.png')
imgM = ImageTk.PhotoImage(imgM)
agregar_btn = tk.Button(root, image=imgM, borderwidth=0, command=lambda: ventanaAtencion())
agregar_btn.grid(column=2, row=0)

#boton Ingresar medico
imgI = Image.open('images/IngresarMedico.png')
imgI = ImageTk.PhotoImage(imgI)
agregar_btn = tk.Button(root, image=imgI, borderwidth=0, command=lambda: ventanaAtencion())
agregar_btn.grid(column=3, row=0)


#Buscar Paciente

tk.Label(root, text = "Buscar Paciente",bg="#0026fe",fg="white",height = 1,font=("Aharoni",12,'bold') ).place(x=92,y=200)
tk.Label(root, text = "rut: ",bg="#0026fe",fg="white",height = 1,font=("Aharoni",12,'bold') ).place(x=45, y=270 )

#Buscar Paciente
buscaPaciente = tk.Entry(root, width=25).place(x=112,y=272)

#boton Datos paciente
imgD = Image.open('images/DatosP.png')
imgD = ImageTk.PhotoImage(imgD)
buscarD = tk.Button(root, image=imgD, borderwidth=0, bg="#0026fe", command=lambda: ventanaAtencion()).place(x= 47, y= 346)

#boton estado paciente
img1 = Image.open('images/EstadoP.png')
img1 = ImageTk.PhotoImage(img1)
buscarE = tk.Button(root, image=img1, borderwidth=0, bg="#0026fe", command=lambda: ventanaAtencion()).place(x= 204, y= 346)


#textBox muestra datos del paciente
datosBox = tk.Text(root, height = 10, width= 35, padx=15,pady=15).place(x=474, y=200)

#boton Limpiar
imgL = Image.open('images/Limpiar.png')
imgL = ImageTk.PhotoImage(imgL)
limpiar = tk.Button(root, image=imgL, borderwidth=0, bg="#0026fe", command=lambda: ventanaAtencion()).place(x= 565, y= 420)

tk.Label(root, text = "Prox. Paciente",bg="#0026fe",fg="white",height = 1,font=("Aharoni",12,'bold') ).place(x=900,y=200)


#textBox prox paciente
proxPacienteBox = tk.Text(root, height = 2, width= 15, padx=15,pady=18).place(x=880, y=230)


tk.Label(root, text = "Lista de Espera",bg="#0026fe",fg="white",height = 1,font=("Aharoni",12,'bold') ).place(x=900,y=310)

#textBox Lista de espera
ListaEsperaBox = tk.Text(root, height = 6, width= 18, padx=15,pady=15).place(x=880, y=350)

#boton siguiente
imgS = Image.open('images/siguiente.png')
imgS = ImageTk.PhotoImage(imgS)
siguiente = tk.Button(root, image=imgS, borderwidth=0, bg="#0026fe", command=lambda: ventanaAtencion()).place(x= 1060, y= 240)












display_logo('./images/logoucen.png',0,0)






root.mainloop()

#agregar_btn = tk.Button(root, text="situacion de pacientes", font=("Aharoni",12,'bold'), bg="#0026fe", fg="white", height=1, width=18)
#otro = tk.Button(root, text="otro", font=("hp simplified",12), bg="#0026fe", fg="white", height=1, width=12,command=lambda:print("click"))
#otro.grid(column=1, row=0, pady=50, padx=100, )


#agregar_btn = tk.Button(root, text="lista de espera", font=("hp simplified",12), bg="#0026fe", fg="white", height=1, width=
#agregar_btn = tk.Button(root, image=display_btn('./images/btn_agregar.png',1,0,20,60,"nw"),borderwidth=0,command="click")