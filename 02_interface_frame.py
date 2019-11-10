'''
    INTERFACE GRAFICA DE PYTHON
'''

# INICIALIZAR UNA LIBRERIA Tkinter
from tkinter import *

# Instanciar clase Tkinter

""" RAIZ """

raiz = Tk()

# Cambiar titulo de la ventana

raiz.title('Primera Interface')

# Controlar el ancho y alto de la ventana con booleanos
raiz.resizable(0,0)

# Cambiar tamaño de la raíz
raiz.geometry('800x600')

# Cambiar el icono de la ventana
# raiz.iconbitmap('static/img/logo.ico')

# Diferentes configuraciónes
raiz.config(bg='red')

""" FRAME """

# Instanciar frames

primerFrame = Frame()
# Empaquetar el frame para que aparezca dentro de raiz
primerFrame.pack()

primerFrame.config(bg='blue')

# Eliminar el tamaño de la raiz con el tamaño del frame

primerFrame.config(width='500', height='400')

# Bordes
primerFrame.config(bd=1)# Ancho de borde
primerFrame.config(relief='solid')#Tipo de borde

# Mover el frame alrededor de la raiz

primerFrame.pack(side='right', anchor='s')

#  LLenar el frame en la raiz(x,y, both)
primerFrame.pack(fill='y', expand='true')

# Cambiar el icono del cursor del raton
primerFrame.config(cursor='pirate')

# Crear un bucle infinito para que la ventana que creemos este escuchando las acciones del usuario permanentemente

raiz.mainloop()