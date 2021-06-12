from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from types import LambdaType
from PIL import Image,ImageTk
from Medico import *
from Paciente import *
from Persona import *
from Especialidad import *
from functions import display_logo




medico = Medico("","","","","","")
paciente = Paciente("","-","-","","","","",False  ,"","","","","","")

# Lista de pacientes
#listaTraumaa = ListaTrauma([paciente])
#listaNeuroo = ListaNeuro([paciente])
#listaCardioo = ListaCardio([paciente])
#listaCompletaa = ListaCompleta([paciente])

listaEnlazada = ListaEnlazada()
listaTrauma = ListaTrauma()
listaNeuro = ListaNeuro()
listaCardio =  ListaCardio()

listaEnlazada.adicionarFinal(Paciente("jose","trauma","M","portugal 272","---","normal","traumatologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("jose","neuro","M","portugal 272","---","normal","neurologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("jose","cardio","M","portugal 272","---","normal","cardiologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("jose","trauma","M","portugal 272","---","normal","traumatologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("jose","neuro","M","portugal 272","---","normal","neurologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("jose","trauma","M","portugal 272","---","normal","cardiologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("jose","trauma","M","portugal 272","---","normal","traumatologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("jose","neuro","M","portugal 272","---","normal","neurologia",False  ,"","","","","",""))
listaEnlazada.adicionarFinal(Paciente("jose","cardio","M","portugal 272","---","normal","cardiologia",False  ,"","","","","",""))



#Lista de medicos
#listaMedicosTrauma = ListaMedicosTrauma([medico])
#listaMedicosTrauma.agregar(Medico("alberto","26970671-6","M","las casas 83","001","Traumatologia",542))
medico = ["alberto","26970671-6","No disponible","No Disponible","543","Traumatologia"]

def tratarPacientes():

    


    
    
    def selectPacient(tabla):

        
        def guardaT():
            
            
            listaEnlazada[index].setDiagnostico(diagnostico.get())
            listaEnlazada[index].setTratamiento(tratamiento.get("1.0","end"))

        
        selected = tabla.focus()
        values = tabla.item(selected, 'values')
        index = int(values[0])
        
        top = Toplevel()
        top.geometry("500x500")
        top.title("tratar")
        

        tk.Label(top, text="Diagnostico:").place(x=40,y=250)
        diagnostico = tk.Entry(top, width=40)
        diagnostico.place(x=170,y=250)

        tk.Label(top, text="Tratamiento:").place(x=40,y=280)
        tratamiento =  tk.Text(top, height = 5, width= 25, padx=15,pady=15)
        tratamiento.place(x=170,y=280)

        guardaB = Button(top, text="guardar", width=50, command=lambda: [print(index), guardaT()])
        guardaB.place(x=200,y=450)

    def printT():
        selected = tablaT.focus()
        values = tablaT.item(selected, 'values')
        index = int(values[0])

        print(listaTrauma[index].getDiagnostico())






    
    roott = Toplevel()
    roott.title("Tratar Paciente")
    roott.geometry("1100x400")
    header = Frame(roott, width = 1200, height = 120, bg = "white")
    header.pack()
    body = Frame(roott, width = 1200, height = 380, bg = "#00B8FF")
    body.pack()

    

    #marco
    marcoTrauma = LabelFrame(roott, text = "Traumatologia",bd = 4 , width = 290 , height = 330, bg = "#EDF0F2")
    marcoTrauma.place(x=30 , y = 25)
    #estilo
    style = ttk.Style()
    style.configure('Treeview', background = "#C0EAF8",foreground = "black", fieldBackground = "#C0EAF8")
    style.theme_use("default")
    style.map('Treeview',background=[('selected','#DCA44C')])
    #creacion de tabla
    tablaT = ttk.Treeview(roott , columns=(0,1, 2), show='headings', height=12)
    tablaT.place(x=50 , y = 50)
    tablaT.tag_configure('oddrow',background="#26C1F4")
    tablaT.tag_configure('evenrow',background="#C0EAF8")
    tablaT.heading(0, text = "N°")
    tablaT.heading(1, text = "Nombre")
    tablaT.heading(2, text = "Rut")
    tablaT.column(0, width = 10, minwidth =25)
    tablaT.column(1, width = 120)
    tablaT.column(2, width = 120)
    #scrollBar
    yscrollbar = ttk.Scrollbar(roott,orient = "vertical", command = tablaT.yview)
    yscrollbar.place(x=300,y=50)
    #yscrollbar.place(x = 300, y =50, fill = Y)

    

   
    #=00=========================================================================================================================================
    #marco
    marcoNeuro = LabelFrame(roott, text = "Neurologia" ,bd = 4 , width = 290 , height = 330, bg = "#EDF0F2")
    marcoNeuro.place(x=380 , y = 25)
    #estilo
    style = ttk.Style()
    style.configure('Treeview', background = "#C0EAF8",foreground = "black", fieldBackground = "#C0EAF8")
    style.theme_use("default")
    style.map('Treeview',background=[('selected','#DCA44C')])
    #creacion de tabla
    tablaN = ttk.Treeview(roott , columns=(0,1, 2), show='headings', height=12)
    tablaN.pack(side="left")
    tablaN.place(x=400 , y = 50)
    tablaN.tag_configure('oddrow',background="#26C1F4")
    tablaN.tag_configure('evenrow',background="#C0EAF8")
    tablaN.heading(0, text = "N°")
    tablaN.heading(1, text = "Nombre")
    tablaN.heading(2, text = "Rut")
    tablaN.column(0, width = 10, minwidth =25)
    tablaN.column(1, width = 120)
    tablaN.column(2, width = 120)

    #scrollBar
    yscrollbar = ttk.Scrollbar(roott,orient = "vertical", command = tablaN.yview)
    yscrollbar.place(x=650,y=50)
    #yscrollbar.place(x = 300, y =50, fill = Y)
    tablaN.configure(yscrollcommand=yscrollbar.set)

    #=======================================================================================================================
     #=00=========================================================================================================================================
    #marco
    marcoCardio = LabelFrame(roott, text = "Cardiologia" ,bd = 4 , width = 290 , height = 330, bg = "#EDF0F2")
    marcoCardio.place(x=730 , y = 25)
    #estilo
    style = ttk.Style()
    style.configure('Treeview', background = "#C0EAF8",foreground = "black", fieldBackground = "#C0EAF8")
    style.theme_use("default")
    style.map('Treeview',background=[('selected','#DCA44C')])
    #creacion de tabla
    tablaC = ttk.Treeview(roott , columns=(0,1, 2), show='headings', height=12)
    tablaC.pack(side="left")
    tablaC.place(x=750 , y = 50)
    tablaC.tag_configure('oddrow',background="#26C1F4")
    tablaC.tag_configure('evenrow',background="#C0EAF8")
    tablaC.heading(0, text = "N°")
    tablaC.heading(1, text = "Nombre")
    tablaC.heading(2, text = "Rut")
    tablaC.column(0, width = 10, minwidth =25)
    tablaC.column(1, width = 120)
    tablaC.column(2, width = 120)

    #scrollBar
    yscrollbar = ttk.Scrollbar(roott,orient = "vertical", command = tablaC.yview)
    yscrollbar.place(x=1000,y=50)
    #yscrollbar.place(x = 300, y =50, fill = Y)
    tablaC.configure(yscrollcommand=yscrollbar.set)
    

    #agregando elementos
    index = 0
    t = 0
    c = 0
    n = 1
    for i in range(0,listaEnlazada.contador()):
        if listaEnlazada[i].getDespacho() == "traumatologia":
            if t % 2 == 0:
                tablaT.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('evenrow'))
                
            else:
                tablaT.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('oddrow'))
                
            t+=1    
        elif listaEnlazada[i].getDespacho() == "cardiologia":
            if index % 2 == 0:
                tablaC.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('evenrow'))
                
            else:
                tablaC.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('oddrow'))        
            c+=1
        else:
            if index % 2 == 0:
                tablaN.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('evenrow'))
                
            else:
                tablaN.insert(parent='', index=i, iid=i, values=(index,listaEnlazada[i].getNombre(), listaEnlazada[i].getRut()), tags = ('oddrow'))    
            n+=1
     
        index += 1
    
    #botones Trauma
    imgL = Image.open('images/btnAM.png')
    imgL = ImageTk.PhotoImage(imgL)
    btnAM = Button(roott, image=imgL, borderwidth=0, bg="#EDF0F2", command =lambda: []  )
    btnAM.place(x = 265, y=310)

    img = Image.open('images/btnD.png')
    img = ImageTk.PhotoImage(img)
    btnD = Button(roott, image=img, borderwidth=0, bg="#EDF0F2", command =lambda: selectPacient(tablaT)  )
    btnD.place(x = 225, y=310)

    imgC = Image.open('images/btnM.png')
    imgC = ImageTk.PhotoImage(imgC)
    btnC = Button(roott, image=imgC, borderwidth=0, bg="#EDF0F2", command =lambda: []  )
    btnC.place(x = 185, y=310)

    #botones Neurologia
    
    imgamN= Image.open('images/btnAM.png')
    imgamN = ImageTk.PhotoImage(imgamN)
    btnAMN = Button(roott, image=imgamN, borderwidth=0, bg="#EDF0F2", command =lambda: []  )
    btnAMN.place(x = 620, y=310)

    imgdn = Image.open('images/btnD.png')
    imgdn = ImageTk.PhotoImage(imgdn)
    btnDn = Button(roott, image=imgdn, borderwidth=0, bg="#EDF0F2", command =lambda: selectPacient(tablaN)  )
    btnDn.place(x = 580, y=310)

    imgmn = Image.open('images/btnM.png')
    imgmn = ImageTk.PhotoImage(imgmn)
    btnMn= Button(roott, image=imgmn, borderwidth=0, bg="#EDF0F2", command =lambda: []  )
    btnMn.place(x = 540, y=310)

    #botones Cradiologia
    
    imgamC= Image.open('images/btnAM.png')
    imgamC = ImageTk.PhotoImage(imgamC)
    btnAMC = Button(roott, image=imgamC, borderwidth=0, bg="#EDF0F2", command =lambda: []  )
    btnAMC.place(x = 970, y=310)

    imgdC = Image.open('images/btnD.png')
    imgdC = ImageTk.PhotoImage(imgdC)
    btnDC = Button(roott, image=imgdC, borderwidth=0, bg="#EDF0F2", command =lambda: selectPacient(tablaN)  )
    btnDC.place(x = 930, y=310)

    imgmC = Image.open('images/btnM.png')
    imgmC = ImageTk.PhotoImage(imgmC)
    btnMC= Button(roott, image=imgmC, borderwidth=0, bg="#EDF0F2", command =lambda: []  )
    btnMC.place(x = 890, y=310)
    
    

    

    
    roott.mainloop()

    


window = Tk()
window.geometry("200x200")
Button(window, text="in", command =lambda: tratarPacientes()).pack()


window.mainloop()