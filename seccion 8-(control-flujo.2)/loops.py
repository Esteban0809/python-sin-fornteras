# Loops = bucles

# While #

i = 0

# while i < 5:
#     i += 1
    # if i == 3:
    #     break
    # La palabra reservada break detendrá la ejecución del bucles
    # if i == 4:
    #     print('El programa finalizará en la siguiente iteración')
    #     continue
    # La palabra reservada continue obviará todas las instrucciones debajo de ella
    # print(i)

# For #

usuarios = ['Chanchito feliz', 'Felipe', 'Roberto', 'Nicolás']

# for usuario in usuarios:
#     print(usuario)

usuario = 'Chanchito feliz'

# for c in usuarios[0]:
#     print(c)


# for usuario in usuarios:
#     if usuario == 'Roberto':
#         break
#     print(usuario)

# for usuario in usuarios:
#     if usuario == 'Roberto':
#         continue
#     print(usuario)

# Range #

# range(numero_inicia, numero_sgte_final, cuanto_aumenta)

# for x in range(3, 30, 3):
#     print(x)
# else: 
#     print('Hemos terminado')
# El else se ejecuta cuando se han iterado todos los elementos

edades = [24, 25, 26, 35]

for usuario in usuarios:
    for edad in edades:
        print(usuario, edad)