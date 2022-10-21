# Función para abrir archivos:
#   open(nombre_archivo, permisos)
#   r = permiso Read, para leer, viene por defecto
#   a = permiso Append, para agregar texto al final del archivo
#   w = permiso Write, para modificar el archivo en su totalidad
#   x = permiso para crear archivos en Python, devolverá un error en caso el 
#   archivo ya exista

# En el caso que queramos abrir un archivo inexistente se creará un nuevo archivo
# con el nombre indicado

# c = open('chanchito.txt', 'w')

# Para leer la totalidad del archivo
# print(c.read())

# Para leer las líneas una por una
# print(c.readline())
# print(c.readline())
# print(c.readline())
# La instrucción readline lee hasta las líneas en blanco

# Iteración más específica por cada una de las líneas
# for x in c:
    # x será cada una de las líneas del archivo
    # print(x)

# \n da un salto de línea
# Si usamos la función write con el permiso de append, agregará líneas al final
# del archivo. Sin embargo, si usamos el permiso de write entonces borrará todo 
# el texto del archivo y lo reemplazará por el que indiquemos
# c.write('\nagregaremos una nueva linea a nuestro archivo')

# Cerrar el archivo con la instrucción close
# c.close()

# x = open('chanchito.txt')

# print(x.read())

# x.close()

# Eliminar archivos

import os

# En caso el archivo no exista lanzará un error
# os.remove('chanchito.txt')

# Para validar la existencia del archivo
if os.path.exists('chanchito.txt'):
    os.remove('chachito.txt')
else:
    print('El archivo no existe')

# Para eliminar un directorio
os.rmdir('micarpet')