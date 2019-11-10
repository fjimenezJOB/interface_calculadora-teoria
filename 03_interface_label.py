from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=500, height= 400)
miFrame.pack()

# Crear un label
miLabel = Label(miFrame, text= 'Hola alumnos de muevete')
miLabel.pack()# Si se utiliza esta opcion el tamaño se ajusta a esto
miLabel.place(x=180, y=10)

# SHorthand crear label
Label(miFrame, text= 'Hola alumnos de muevete').place(x=180, y=10)

# Opciones en label
Label(miFrame, text= 'Hola alumnos de muevete',fg='red', font=('Arial',20)).place(x=180, y=10)

# Label de img
miImagen = PhotoImage(file='static/img/giphy.gif')
Label(miFrame, image= miImagen).place(x=0, y=0)


raiz.mainloop()