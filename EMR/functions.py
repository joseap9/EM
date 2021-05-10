import tkinter as tk

from PIL import Image,ImageTk

def display_logo(url,row,column):
    img = Image.open(url)
    img = img.resize((int(img.size[0]/1.5),int(img.size[1]/1.5)))
    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(image = img , bg="white")
    img_label.Image = img
    img_label.grid(column=column,row=row,rowspan=4 , padx=20,pady=40 , sticky = "nw")

def display_btn(url,column,row,padx,pady,sticky):
    img = Image.open(url)
    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(image=img, bg="white")
    img_label.Image = img
    img_label.grid(column=column,row=row, padx=padx,pady=pady, sticky = sticky)

def display_btnn(url,x,y):
    img = Image.open(url)
    img = ImageTk.PhotoImage(img)
    



