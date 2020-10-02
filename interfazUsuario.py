from tkinter import *

ventana = Tk()
ventana.title("Ventanisima")
ventana.geometry("600x300")

etiqueta = Label(ventana, text= "Esto es la primera etiqueta")
etiqueta.pack()

segundoEtiqueta = Label(ventana, text= "Esta es la segunda etiqueta")
segundoEtiqueta.pack()

ingresoTexto = Entry(ventana)
ingresoTexto.pack()

boton = Button(ventana, text="Push")
boton.pack()

ventana.mainloop()