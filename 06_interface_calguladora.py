from tkinter import *

raiz = Tk()

# ********** FUNCION ************

# Variables Globales
primeraVez = False
resultado = 0
operacion = ''
operador = ''
numeroVisor = StringVar()


def suma(num):
    global operacion
    global resultado
    global operador
    operacion = 'sumar'
    operador = 'sumar'
    resultado += float(num)
    numeroVisor.set(resultado)


def resta(num):
    global operacion
    global resultado
    global operador

    resultado -= float(num)
    operacion = 'restar'
    operador = 'restar'
    numeroVisor.set(abs(resultado))
    resultado *= -1


def multiplica(num):
    global operacion
    global resultado
    global operador
    global primeraVez

    if resultado == 0 and primeraVez == False:
        primeraVez = True
        resultado = 1

    resultado *= float(num)
    operacion = 'multiplicar'
    operador = 'multiplicar'
    numeroVisor.set(resultado)


def divide(num):
    global operacion
    global operador
    global resultado
    global primeraVez

    operacion = 'dividir'
    operador = 'dividir'

    if resultado == 0 and primeraVez == False:
        resultado = float(num)
    else:
        resultado/= float(num)


    numeroVisor.set(resultado)


def borrar():
    global resultado
    global primeraVez
    resultado = 0
    primeraVez = False
    numeroVisor.set('0')


def respuesta(num):
    global resultado

    if operador == 'sumar':
        total = resultado + float(numeroVisor.get())
        numeroVisor.set(total)

    if operador == 'restar': 
        if (resultado - float(num)) > 0:
            total = abs(resultado - float(numeroVisor.get()))
            numeroVisor.set(total)
    
    if operador == 'multiplicar':
        total = resultado * float(num)
        numeroVisor.set(total)

    if operador == 'dividir':
        total = resultado / float(num)
        numeroVisor.set(total)
   


def pulsarNumero(num):
    global operacion
    global numeroVisor

    if numeroVisor.get() == '0':
        numeroVisor.set('')

    if operacion != '':
        numeroVisor.set(num)
        operacion = ''
    else:
        numeroVisor.set(numeroVisor.get() + num)


# ********************************
miFrame = Frame(raiz, width=1000, height=500)
miFrame.pack()
raiz.resizable(0, 0)
raiz.title('VOLTEX - Calculadora')

# Visor
visor = Entry(miFrame, textvariable=numeroVisor)
visor.grid(row=0, column=0,  columnspan=4)
visor.config(bg='#2B2A33', fg='white', justify='right', font=('Arial', 21))

# Boton Numeros
botonCero = Button(miFrame, text='0', width=9, height=1,
                   command=lambda: pulsarNumero('0'))
botonCero.grid(row=5, column=0, columnspan=2)
botonCero.config(bg='#56585E', font=('Arial', 20))

botonUno = Button(miFrame, text='1', width=4, height=1,
                  command=lambda: pulsarNumero('1'))
botonUno.grid(row=4, column=0)
botonUno.config(bg='#56585E', font=('Arial', 20))

botonDos = Button(miFrame, text='2', width=4, height=1,
                  command=lambda: pulsarNumero('2'))
botonDos.grid(row=4, column=1)
botonDos.config(bg='#56585E', font=('Arial', 20))

botonTres = Button(miFrame, text='3', width=4, height=1,
                   command=lambda: pulsarNumero('3'))
botonTres.grid(row=4, column=2)
botonTres.config(bg='#56585E', font=('Arial', 20))

botonCuatro = Button(miFrame, text='4', width=4, height=1,
                     command=lambda: pulsarNumero('4'))
botonCuatro.grid(row=3, column=0)
botonCuatro.config(bg='#56585E', font=('Arial', 20))

botonCinco = Button(miFrame, text='5', width=4, height=1,
                    command=lambda: pulsarNumero('5'))
botonCinco.grid(row=3, column=1)
botonCinco.config(bg='#56585E', font=('Arial', 20))

botonSeis = Button(miFrame, text='6', width=4, height=1,
                   command=lambda: pulsarNumero('6'))
botonSeis.grid(row=3, column=2)
botonSeis.config(bg='#56585E', font=('Arial', 20))

botonSiete = Button(miFrame, text='7', width=4, height=1,
                    command=lambda: pulsarNumero('7'))
botonSiete.grid(row=2, column=0)
botonSiete.config(bg='#56585E', font=('Arial', 20))

botonOcho = Button(miFrame, text='8', width=4, height=1,
                   command=lambda: pulsarNumero('8'))
botonOcho.grid(row=2, column=1)
botonOcho.config(bg='#56585E', font=('Arial', 20))

botonNueve = Button(miFrame, text='9', width=4, height=1,
                    command=lambda: pulsarNumero('9'))
botonNueve.grid(row=2, column=2)
botonNueve.config(bg='#56585E', font=('Arial', 20))

# Botones Operaciones
multiplicar = Button(miFrame, text='X', width=4, height=1,
                     command=lambda: multiplica(numeroVisor.get()))
multiplicar.grid(row=2, column=3)
multiplicar.config(bg='#FF8A08', font=('Arial', 20))

dividir = Button(miFrame, text='/', width=4, height=1,
                 command=lambda: divide(numeroVisor.get()))
dividir.grid(row=1, column=3)
dividir.config(bg='#FF8A08', font=('Arial', 20))

ac = Button(miFrame, text='AC', width=4, height=1, command=lambda: borrar())
ac.grid(row=1, column=0)
ac.config(bg='#3C3B45', font=('Arial', 20))

comas = Button(miFrame, text=',', width=4, height=1,
               command=lambda: pulsarNumero('.'))
comas.grid(row=5, column=2)
comas.config(bg='#56585E', font=('Arial', 20))

masmenos = Button(miFrame, text='+/-', width=4, height=1,
                  command=lambda: pulsarNumero('+/-'))
masmenos.grid(row=1, column=1)
masmenos.config(bg='#3C3B45', font=('Arial', 20))

porciento = Button(miFrame, text='%', width=4, height=1,
                   command=lambda: pulsarNumero('%'))
porciento.config(bg='#3C3B45', font=('Arial', 20))
porciento.grid(row=1, column=2)

sumar = Button(miFrame, text='+', width=4, height=1,
               command=lambda: suma(numeroVisor.get()))
sumar.grid(row=3, column=3)
sumar.config(bg='#FF8A08', font=('Arial', 20))

restar = Button(miFrame, text='-', width=4, height=1,
                command=lambda: resta(numeroVisor.get()))
restar.grid(row=4, column=3)
restar.config(bg='#FF8A08', font=('Arial', 20))

igual = Button(miFrame, text='=', width=4, height=1,
               command=lambda: respuesta(numeroVisor.get()))
igual.grid(row=5, column=3)
igual.config(bg='#FF8A08', font=('Arial', 20))

raiz.mainloop()
