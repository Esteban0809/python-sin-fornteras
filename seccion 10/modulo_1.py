# Importar módulos #
# Para importar archivos se usa la palabra reservada import
# No es necesario agregar la extensión del archivo

# import modulos

# print (modulos.mascotas)

# modulos.saludo('Lalito')

# Renombrando módulos #

# import modulos as xs

# Seleccionando lo importado #

from modulos import saludo, mascotas
# Módulo instalado con pip3 
from camelcase import CamelCase 

# print (xs.mascotas)
print(mascotas)
saludo('Lalito')

c = CamelCase()

s = 'esta oración necesita CamelCase!'

camelcased =  c.hump(s)

print(camelcased)

# COMANDOS PIP #

# Instalar 
# pip3 install modulo

# Desinstalar 
# pip3 uninstall modulo

# Listar
# pip3 list