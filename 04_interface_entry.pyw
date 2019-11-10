from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width= 1000, height=500, padx = 20, pady = 20)
miFrame.pack()

# Entry es un cuadro de texto
nombreLabel = Label(miFrame, text='Nombre:')
nombreLabel.grid(row=0, column=0, padx=5, pady=0, sticky='e')

cuadroNombre= Entry(miFrame)
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg='blue')

# ****

emailLabel = Label(miFrame, text='Email:')
emailLabel.grid(row=1, column=0, padx=5, pady=0, sticky='e')


cuadroEmail= Entry(miFrame)
cuadroEmail.grid(row=1, column=1)
cuadroEmail.config(fg='blue')

# ****

passLabel = Label(miFrame, text='Password:')
passLabel.grid(row=2, column=0, padx=5, pady=0, sticky='e')


cuadroPass= Entry(miFrame)
cuadroPass.grid(row=2, column=1)
cuadroPass.config(fg='red', justify='center', show='*')

raiz.mainloop()