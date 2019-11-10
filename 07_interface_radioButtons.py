from tkinter import *

raiz = Tk()

# Contenedor del valor
opcion = IntVar()


# Funcion
def imprimir():
    if opcion.get() == 1:
        etiqueta.config(text='Eres un Machote')
    else:
        etiqueta.config(text='Eres una señorita')
    


Label(raiz, text='Genero').pack()

# Boton radio button
Radiobutton(raiz, text='Masculino', variable= opcion, value=1, command=imprimir).pack()
Radiobutton(raiz, text='Femenino', variable= opcion, value=2, command=imprimir).pack()

# Visualizacion de la app
etiqueta = Label(raiz)
etiqueta.pack()


raiz.mainloop()