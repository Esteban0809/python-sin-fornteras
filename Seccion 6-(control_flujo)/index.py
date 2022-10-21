# Condicionales

# if 2 < 5:
#     print("2 es menor que 5")

# Comparación de igualdad ==
# Comparación de diferencia !=
# Comparación menor <
# Comparación mayor >
# Comparación menor igual <=
# Comparación mayor igual >=

# if 2 == 2:
#     print('2 es igual a 2')
    
# if 2 == 3:
#     print('2 es igual a 3')

# if 2 > 5: 
#     print('2 es mayor a 5')

# if 5 > 2: 
#     print('5 es mayor a 2')

# if 2 != 2:
#     print('2 es distinto a 2')

# if 3 != 2:
#     print('3 es distinto a 2')

# if 3 >= 2:
#     print('3 es mayor o igual a 2')

# if 3 >= 3:
#     print('3 es mayor o igual a 3')


# Elif, Else #

if 2 > 5:
    print('2 menor a 5 en if')
elif 2 > 5:
    print('2 menor a 5 en elif')
elif 2 < 5:
    print('2 menor a 5 en segundo elif')
else:
    print('yo me imprimo solo si todo lo anterior es falso')

# No es obligatorio que exista un elif entre el if y el else

# If cortos #

if 2 < 5: print('If de una linea')

# Operador ternario #

# Operacion en caso verdadero IF condicion ELSE Operacion en caso falso

print('Cuando devuelve true') if 5 > 2 else print('Cuando devuelve false')

# And y or #

# And requiere que ambas condiciones sean verdaderas para retornar verdadero

if 2 < 5 and 3 > 2:
    print('ambas devuelven true')

# Or requiere que al menos una de las condiciones sea verdadera para retornar verdadero

if 2 > 5 or 3 > 2:
    print('devolvera true')