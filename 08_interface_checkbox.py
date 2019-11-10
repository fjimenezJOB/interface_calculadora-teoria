from tkinter import *

raiz = Tk()


raiz.title('Que estación te gusta mas??')
raiz.geometry('900x700')
raiz.resizable(20,20)

miFrame = Frame()
miFrame.pack(side='bottom')

etiqueta1 = Label(miFrame)
etiqueta1.pack()

etiqueta2 = Label(miFrame)
etiqueta2.pack()

etiqueta3 = Label(miFrame)
etiqueta3.pack()

etiqueta4 = Label(miFrame)
etiqueta4.pack()

# Variables
varVerano = IntVar()
varInvierno = IntVar()
varPrimavera = IntVar()
varOtoño = IntVar()


def opciones():
    opcionSelec = ''

    if varVerano.get() == 1:
        opcionSelec += 'Te gusta el verano y el calorcito\n'

    if varInvierno.get() == 1:
        opcionSelec += 'Te gusta el invierno y el fresquito\n'

    if varPrimavera.get() == 1:
        opcionSelec += 'Te gusta la primavera y las flores\n'

    if varOtoño.get() == 1:
        opcionSelec += 'Te gusta el otoño y las hojas\n'

    frase.config(text=opcionSelec, fg='red', font=('Arial', 20))


# Crear una imagen
imagen = PhotoImage(file='static/img/estaciones.png')
Label(raiz, image=imagen).place(x=0, y=0)

# Zona del checkbox
Label(miFrame, text='¿Que estación te gusta mas?', font=('Arial', 20)).pack()
Checkbutton(miFrame, text='Verano', variable=varVerano,
            onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(miFrame, text='Invierno', variable=varInvierno,
            onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(miFrame, text='Primavera', variable=varPrimavera,
            onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(miFrame, text='Otoño', variable=varOtoño,
            onvalue=1, offvalue=0, command=opciones).pack()

frase = Label(miFrame)
frase.pack()

raiz.mainloop()