'''
La funcion lambda
-------------------
Es una funcion anónima y que se utiliza en python para abreviar,
resumir, una función normal a la mínima expresión
Serian las funciones de tamaño pequeño, la podemos pasar a lambda

'''

# Funcion standard


def primer_triangulo(base, altura):
    return(base * altura) / 2

# funcion lambda


def triangulo(base, altura): return (base * altura) / 2


print(triangulo(4, 4))

# *************************************************


def elevado_al_cubo(numero): return numero**3


print(elevado_al_cubo(10))

# *************************************************

comission = 1500


def valor_comision(comission): return "¡{}!".format(comission)


print(valor_comision(comission))
