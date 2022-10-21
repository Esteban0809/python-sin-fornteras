# Strings #

# Se puede usar tanto las comillas simples como las dobles

palabra = 'hola mundo' # string
oracion = 'hola mundo comilla doble'

entero = 20 # integer
con_decimales = 20.2 # float
complejo = 1j # es necesario utilizar una j al final de una variable de numero complejo

#print (palabra, oracion, entero, con_decimales, complejo)

# Listas #

#lista = [1, 2, 3] 
lista = ['Hola', 'Mundo', 'Chanchito feliz']

# Al imprimir una lista vacia solo se muestran los corchetes: []

# Para copiar una lista a otra:
lista2 = lista.copy()

# Para agregar un elemento a la lista:
#lista.append(4)
lista.append('Chanchito triste')

# Para eliminar todos los elementos de la lista:
#lista.clear()

#print(lista, lista2)

# Para contar la cantidad de repeticiones de un elemento de la lista:
#print(lista2.count(3))

# Para contar los elementos de la lista:
#print(len(lista2))
largo_lista = len(lista)
#print(largo_lista)

# Para acceder a los elementos de la lista:
# print(lista[0])
# Siempre se utilizan indices y no la posición del elemento

# Para borrar el último elemento de la lista:
# lista.pop()
# print(lista)

# Para eliminar un elemento en concreto
# lista.remove('Hola')
# print(lista)

# Para revertir el orden de la lista:
# lista.reverse()
# print(lista)

# Para ordenar la lista en orden ascendente:
lista.sort()
# print(lista)

# Tuplas #

# A diferencia de las listas, no puedes modificar a las tuplas

tupla = ('Hola','mundo','somos','tupla')
# print(tupla)

# Para contar la cantidad de repeticiones de un elemento de la tupla:
# print(tupla.count('mundo'))

# # Para devolver el índice del elemento:
# print(tupla.index('mundo'))

# Como las tuplas no se pueden modificar se deben de castear a una lista
# lista_de_tupla = list(tupla)
# lista_de_tupla.append('Chanchito')
# print(lista_de_tupla)

# Rangos #

rango = range(6)
# print(rango)

# Diccionarios #

diccionario =  {
        "nombre" : "Mishifu",
        "raza" : "Persa",
        "edad" : 5
        }

# print(diccionario)
# Para acceder a un valor se debe digitar la llave entre corchetes:
# print(diccionario['nombre'])
# Sin embargo un método para acceder a los valores es:
# print(diccionario.get('nombre'))

# Para modificar algún valor:
diccionario['nombre'] = 'MishiGod'
# print(diccionario)

# Para saber la cantidad de elementos:
# print(len(diccionario))

# Para agregar una llave con su valor:
diccionario['ronronea'] = 'Si'
# print(diccionario)

# Para eliminar una propiedad(llave y valor):
# diccionario.pop('raza')
# o 
# del diccionario['ronronea']

# Para eliminar la última propiedad ingresada al diccionario:
# diccionario.popitem()

# Para copiar el diccionario:
# copia_gato = diccionario.copy()
# Otra forma:
copia_gato = dict(diccionario)
del diccionario['ronronea']

# Para limpiar el diccionario:
diccionario.clear()

# print(diccionario, copia_gato)

# Diccionarios anidados
# Primer forma:

# gatitos = {
#         "Fluffy" : {
#             "nombre" : "Fluffy",
#             "edad" : 4,
#             },
#         "Mamba" : {
#             "nombre" : "Black Mamba",
#             "edad" : 12,
#             }
#         }

# Segunda forma:

fluffy = {
        "nombre" : "Fluffy",
        "edad" : 4
        }

mamba = {
        "nombre" : "Black Mamba",
        "edad" : 12
        }

gatitos = {
        "Fluffy" : fluffy,
        "Mamba" : mamba
        }

# print(gatitos)

# Constructor dict

perritos = dict(nombre = "Chanchito feliz", edad = 5)
print(perritos)

# Ambas sintaxis para crear diccionarios son válidas y ninguna es mejor que la otra

# Booleanos #

# La primera letra debe ir con mayúscula

verdadero = True
falso = False

print(verdadero, falso)