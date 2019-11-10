'''
    INTERFACE GRAFICA DE PYTHON
'''

# INICIALIZAR UNA LIBRERIA Tkinter
from tkinter import *

# Instanciar clase Tkinter

raiz = Tk()

# Cambiar titulo de la ventana

raiz.title('Primera Interface')

# Controlar el ancho y alto de la ventana con booleanos
raiz.resizable(0,0)

# Cambiar tamaño de la raíz
raiz.geometry('800x600')

# Cambiar el icono de la ventana
raiz.iconbitmap('static/img/logo.ico')

# Diferentes configuraciónes
raiz.config(bg='red')

# Crear un bucle infinito para que la ventana que creemos este escuchando las acciones del usuario permanentemente

raiz.mainloop()