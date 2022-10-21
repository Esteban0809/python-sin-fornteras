# Input #
# Es la función utilizada para solicitar datos al usuario

# dato = input('Ingrese dato: ')
# print(dato)

# lista = ['hola', 'mundo', 'chanchito', 'feliz', 'dragones']

# if lista.count(dato) > 0:
#     print('El dato existe:', dato)
# else:
#     print('El dato no existe:', dato)


# Ejercicio: Calculadora para sumar

primero = input('Ingrese el primer número: ')

# Validación de errores #

# El try, como indica su nombre, intetará realizar una acción, la indicada en la identación, pero
# en caso dicha acción provoque un error pasará a la siguiente acción especificada en el except

try:
    primero = int(primero)
except:
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('El valor ingresado no es un número')
    exit()


segundo = input('Ingrese el segundo número: ')

try:
    segundo = int(segundo)
except:
    segundo = 'chanchito feliz'

if segundo == 'chanchito feliz':
    print('El valor ingresado no es un número')
    exit()

# if primero == 'chanchito feliz' or segundo == 'chanchito feliz':
#     print('Ingresaste mal un dato, prueba solo con números') 
# else:
#     print(primero + segundo)

simbolo = input('Ingrese la operación: ')

if simbolo ==  '+':
    print('Suma:', primero + segundo)
elif simbolo == '-':
    print('Resta:', primero - segundo)
elif simbolo == '*':
    print('Multiplicación:', primero * segundo)
elif simbolo == '/':
    print('División:', primero / segundo)
else:
    print('Simbolo incorrecto!')

# Esto concatenaría los strings
# print(primero + segundo)

# Para sumar los dos números introducidos debemos realizar un casting a enteros
# print(int(primero) + int(segundo))