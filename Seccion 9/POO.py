# La convención en todos los lenguajes de programación es escribir
# la primera letra en mayúscula

# POO #
# Init #

# El __init__ es su constructor y el self seria el this
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    # nombre = "Jose"
    # apellido = 'Garcia'

    def saludo(self):
        print('Hola!, mi nombre es', self.nombre, self.apellido)
    # Se puede usar cualquier nombre en lugar de "self", pero al momento de 
    # desarrollar en equipos esto puede ser un problema. Por ello, es mejor 
    # mantener la convención del "self"
    # def saludo(this):
    #     print('Hola!, mi nombre es', this.nombre, this.apellido)

# Para crear un objeto de la clase:
# variable = Clase(parametros)

usuario = Usuario('Jose', 'Garcia')
usuario2 = Usuario('Lalo', 'Lecav')

# print(usuario.nombre, usuario.apellido)
# usuario.saludo()

# print(usuario2.nombre, usuario2.apellido)
# usuario2.saludo()

# Manipulación de las instancias posteriormente a la creación del objeto
usuario2.nombre = 'Chetan'
# usuario2.saludo()

# Eliminación de las instancias
# del usuario2.nombre
# usuario2.saludo()

# Eliminación del objeto
# del usuario
# print(usuario)


# Herencia #

# Para realizar la Herencia
# class clase_hijo(clase_padre):

class Admin(Usuario):
    def super_saludo(self):
        print('Hola!, mi nombre es', self.nombre, self.apellido, 'y soy administrador')

# La clase hijo reutiliza el método init de la clase padre

admin = Admin('Super', 'Feliz')
# Podemos acceder a los métodos de la clase padre desde la clase hijo
# admin.saludo()
# admin.super_saludo()


# Ejercicio #

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola, soy un', self.tipo ,'y mi sonido es el', self.onomatopeya)
    # En el video se uso el "self.tipo", ya que posteriormente es un atributo declarado
    # en las clases. Sin embargo, esto no me convence por completo, a mi parecer está mal 
    # realizado y en lugar de eso debería haberse creado un atributo tipo el cual se asignaba
    # en el método __init__ 

class Gato(Animal):
    tipo = 'gato'
    # Para extender el método __init__ del padre se tiene que crear el método __init__ para 
    # el hijo, llamar al método __init__ del padre y posteriormente añadir el código extendido
    def __init__(self, nombre, onomatopeya):
        # El método __init__ requiere de sus parámetros originales
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola, soy un gato extendido')

class Perro(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        # La palabra reservada "super()" hace referencia a la clase padre, pero en este caso
        # no es necesario la referencia a la instancia "self"
        super().__init__(nombre, onomatopeya)
        print('Instanciando un perro')

class Canario(Animal):
    tipo = 'canario'

gato = Gato('Fluffy', 'maullido')
gato.saludo()

perro = Perro('Firulais', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silbido')
canario.saludo()