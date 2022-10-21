# Ejercicio 1 #
# Multiplicar dos números sin usar el símbolo de la multiplicación

# n1 = int(input('Ingrese el primer número: '))
# n2 = int(input('Ingrese el primer número: '))

n1 = 4
n2 = 8
resultado = 0

for i in range(n2):
    resultado += n1

print(resultado)


# Ejercicio 2 #
# Ingresar un nombre y apellido y escribirlo al revés

nombre = 'Chanchito'
apellido = 'Feliz'

nombre_completo = nombre + ' ' + apellido

# Forma 1
for i in range(len(nombre_completo) - 1, -1, -1):
    print(nombre_completo[i], end = '')

# Forma 2
# Operación de slice:
print(nombre_completo[::-1])


# Ejercicio 3 #
# Encontrar una función que encuentre el menor elemento de una lista

lista = [1, 2, 55, -24, -13, 23]

def menor_valor(lista):
    menor = lista[0]
    # for i in range(1, len(lista)):
    #     if menor >= lista[i]:
    #         menor = lista[i]
    for x in lista:
        if menor >= x:
            menor = x
    return menor

def menor_valor_sv(lista):
    menor = 'init'
    for x in lista:
        if menor == 'init':
            menor = x
        else:
            menor = x if x < menor else menor
    return menor

print(menor_valor(lista))
print(menor_valor_sv(lista))


# Ejercicio 4 #
# Escribir una función que devuelva el volumen de una ésfera por su radio
# 4/3 * pi * radio ** 3

from math import pi
from platform import architecture

def volumen_esfera(radio):
    volumen = 4 / 3 * pi * radio ** 3
    return volumen

print(volumen_esfera(3))


# Ejercicio 5 #
# Escribir una función que indique si el usuario (objeto) es mayor de edad

def mayor_edad(edad):
    return edad >= 18

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario = Usuario(12)
usuario2 = Usuario(21)

resultado1 = mayor_edad(usuario.edad)
resultado2 = mayor_edad(usuario2.edad)

print(resultado1, resultado2)


# Ejercicio 6 #
# Escribir una función que indique si es un número par o impar

def num_par(numero):
    return numero % 2 == 0

rpta1 = num_par(12)
rpta2 = num_par(13)
print(rpta1, rpta2)


# Ejercicio 7 #
# Escribir una función que cuente cuantas vocales tiene una palabra #

def contador_vocales(palabra):
    vocales = ['a', 'e', 'i', 'o', 'u']

    contador = 0
    for i in palabra:
        vocal = i.lower()
        for j in vocales:
            if j == vocal:
                contador += 1
        
    return contador

print(contador_vocales('estA Es una orAcion de prUeba'))


# Ejercicio 8 #
# Escribir una aplicación que reciba una cantidad infinita de números hasta
# decir basta, luego que devuelva la suma de números ingresados

suma = 0
var = 0

print('Ingrese números y para salir ingrese "basta"')

while var != 'basta':
    var = input('Ingresa un número: ')
    try:
        num = int(var)
        suma += num
    except:
        var = var.lower()
        
print(suma)


# Ejercicio 9 #
# Escribir una función que recibe nombre y apellido y los vaya agregando a un archivo

def agregar_nombre_apellido(nombre, apellido):
    archivo = open('nombre_apellido.txt', 'a')
    archivo.write(nombre + ' ' + apellido + '\n')
    archivo.close()

agregar_nombre_apellido('Juan', 'Gonzales')
archivo = open('nombre_apellido.txt')
print(archivo.read())