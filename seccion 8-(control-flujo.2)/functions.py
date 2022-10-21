# Funciones #

def mi_funcion():
    print("Esta es mi primera función")

# mi_funcion()

# El dato recibido por una función, dentro de la misma, es llamado argumento
def print_data(primer_argumento):
    print('mi argumento es', primer_argumento)

# Al momento de pasar un dato a una función lo llamaremos parámetro
# print_data('Primer Parámetro')

# def imprimir_oracion(nombre):
#     print('El nombre completo es', nombre)

# imprimir_oracion('Chanchito', 'feliz')

# En el caso que se vaya a pasar una cantidad indeterminada de datos 
# como argumentos, se puede usar el asterisco para indicarlo, esto hará
# que los elementos que los argumentos recibidos sean parte de una tupla
def imprimir_oracion(*nombre):
    # En caso se quiera acceder a un solo elemento de la tupla se usa:
    # print('El nombre completo es', nombre[0])
    print('El nombre completo es', nombre)

# imprimir_oracion('Chanchito', 'feliz', 'heroico')


def nombre_completo(apellido, nombre):
    print(nombre, apellido)

# En caso no se acuerden el orden de los argumentos se puede pasar como
# parámetro el nombre de las variables asignandoles sus respectivos valores
# nombre_completo(nombre = 'Chanchito', apellido = 'feliz')

# Para agrupar y acceder a los datos como si fuera un diccionario:
def nombre_completo2(**kwargs):
    print(kwargs['nombre'], kwargs['apellido'])

# nombre_completo2(nombre = 'Chanchito', apellido = 'Feliz')

# Argumento por defecto
def mi_funcion2(default_argument = 'Chanchito'):
    print(default_argument)

# mi_funcion2('Batman')
# mi_funcion2()

# Listas como parámetros
def mi_funcion_lista(lista):
    for el in lista:
        print(el)

# mi_funcion_lista(['Chanchito', 'feliz'])

def concatena_nombres(lista):
    i = ''
    for el in lista:
        i = i + el + ' '
    return i

# nombres = concatena_nombres(['Chanchito', 'feliz'])
# print(nombres)

# Acercamiento a Recursividad #

def recursion(i):
    if (i < 1):
        return i
    print(i)
    recursion(i - 1)

recursion(6)

# Cuándo sirve la recursividad?
# Cuando trabajemos sobre una colección de datos o cuando se requiera
# hacer reintentos para llamar a un servidor o una base de datos en caso de 
# que esta falle