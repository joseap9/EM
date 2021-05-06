from Paciente import *
import tkinter as tk

paciente = Paciente("","","","","","","","")
sexos= ["masculino","femenino","otro"]
estados=["reanimacion","emergencia","urgencia","prioritario","no urgencia"]
#despachos=["traumatologia","neurologia","cardiologia"]


def ventanaAtencion():



    def btnAgregar():

        paciente.solicitarAtencion(nombre.get(),rut.get(),sexo.get(),direccion.get(),diagI.get(), estado.get(), "", "")



    def btnMostrar():
        paciente.muestra()

    def close_window(root):
        root.destroy()

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
    tk.Radiobutton(root, value="Traumatologia", variable=despacho, text="Traumatologia").place(x=170,y=210)
    tk.Radiobutton(root, value="neurologia", variable=despacho, text="neurologia").place(x=170,y=230)
    tk.Radiobutton(root, value="cardiologia", variable=despacho, text="cardiologia").place(x=170,y=250)
    

    #tk.Label(root, text="numero de atencion:").grid(pady=5, row=6, column=0)
    #numAtencion = tk.Entry(root, width=40)
    #numAtencion.grid(padx=5, row=6, column=1)

    agregar = tk.Button(root, text="Agregar", width=50, command=lambda: [btnAgregar(), close_window(root), btnMostrar()])
    agregar.place(x=50,y=300)

    #mostrar = tk.Button(root, text="Listado de Pacientes", width=50, command=lambda: btnMostrar())
    #mostrar.grid(padx=10, pady=10, row=7, column=0, columnspan=2)

    root.mainloop()










