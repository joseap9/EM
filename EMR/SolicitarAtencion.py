from Paciente import *
import tkinter as tk

paciente = Paciente("","","","","","","")


def ventanaAtencion():



    def btnAgregar():

        paciente.solicitarAtencion(nombre.get(),rut.get(),sexo.get(),direccion.get(),estado.get(), camaAsig.get(), numAtencion.get())



    def btnMostrar():
        paciente.muestra()

    def close_window(root):
        root.destroy()

    root = tk.Tk()
    root.title("Solicitar Atencion")
    root.geometry("450x450")

    tk.Label(root, text="Nombre:").grid(pady=5, row=0, column=0)
    nombre = tk.Entry(root, width=40)
    nombre.focus()
    nombre.grid(padx=5, row=0, column=1)


    tk.Label(root, text="rut:").grid(pady=5, row=1, column=0)
    rut = tk.Entry(root, width=40)
    rut.grid(padx=5, row=1, column=1)

    tk.Label(root, text="sexo:").grid(pady=5, row=2, column=0)
    sexo=""
    tk.Radiobutton(root, text="M", variable=sexo, value="masculino").grid(padx=5, row=2, column=1)




    tk.Label(root, text="direccion:").grid(pady=5, row=3, column=0)
    direccion = tk.Entry(root, width=40)
    direccion.grid(padx=5, row=3, column=1)

    tk.Label(root, text="cama Asignada:").grid(pady=5, row=4, column=0)
    camaAsig = tk.Entry(root, width=40)
    camaAsig.grid(padx=5, row=4, column=1)

    tk.Label(root, text="estado:").grid(pady=5, row=5, column=0)
    estado = tk.Entry(root, width=40)
    estado.grid(padx=5, row=5, column=1)

    tk.Label(root, text="numero de atencion:").grid(pady=5, row=6, column=0)
    numAtencion = tk.Entry(root, width=40)
    numAtencion.grid(padx=5, row=6, column=1)

    agregar = tk.Button(root, text="Agregar", width=50, command=lambda: [btnAgregar(), close_window(root)])
    agregar.grid(padx=10, pady=10, row=8, column=0, columnspan=2)

    mostrar = tk.Button(root, text="Listado de Pacientes", width=50, command=lambda: btnMostrar())
    mostrar.grid(padx=10, pady=10, row=7, column=0, columnspan=2)

    root.mainloop()










